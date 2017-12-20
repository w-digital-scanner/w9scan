import re
import sys
import socket

_SUPPORT_SSL = False
try:
    import ssl

    _SUPPORT_SSL = True
except:
    pass

import urlparse
import urllib
import base64
import time
import zlib
import gzip
import StringIO
import Cookie
import cookielib
import shlex
import argparse
from argparse import Namespace

DEF_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)'
RECV_PACKET_LEN = 1024
RE_KEEPALIVE_TIMEOUT = re.compile('timeout=(\\d+)')
RE_MIME_TYPE = re.compile('([^\\s;]+)', re.I)


class CurlError(Exception):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return repr(self.code)


class Curl(object):
    CURLE_OK = 0
    CURLE_COULDNT_CONNECT = 1
    CURLE_OPERATION_TIMEDOUT = 2
    CURLE_RECV_ERROR = 3
    CURLE_SEND_ERROR = 4
    CURLE_FILESIZE_EXCEEDED = 5
    CURLE_COULDNT_RESOLVE_HOST = 6
    CURLE_UNSUPPORTED_PROTOCOL = 7
    CURLE_ARG_ERROR = 8
    CURLE_MIME_ERROR = 9

    def __init__(self, sniff_func=None, init_cookie=None, user_agent=None, plugin_id=-1, log_func=None):
        self._conn = None
        self._buf = ''
        self.sniff_func = sniff_func
        self._redirs = 0
        self._transfer_start_time = 0
        self._max_time = 0
        self._received_size = 0
        self._max_filesize = 0
        self._conn_pool = {}
        self._timeout_pool = {}
        self._cookie_pool = {}
        self._init_cookie = init_cookie
        self._max_error = 10
        self._error_count = 0
        self.plugin_id = plugin_id
        self.log_func = log_func
        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-I', '--head', action='store_true')
        group.add_argument('-d', '--data', action='append')
        parser.add_argument('-A', '--user-agent', default=user_agent or DEF_USER_AGENT)
        parser.add_argument('-b', '--cookie')
        parser.add_argument('--connect-timeout', type=int, default=10)
        parser.add_argument('-e', '--referer')
        parser.add_argument('-H', '--header', action='append')
        parser.add_argument('-i', '--include', action='store_true')
        parser.add_argument('-m', '--max-time', type=int, default=0)
        parser.add_argument('--max-filesize', type=int)
        parser.add_argument('--mime-type')
        parser.add_argument('-L', '--location', action='store_true')
        parser.add_argument('--max-redirs', type=int, default=5)
        parser.add_argument('-T', '--upload-file', action='store_true')
        parser.add_argument('--retry', type=int, default=2)
        parser.add_argument('--retry-delay', type=int, default=1)
        parser.add_argument('-u', '--user')
        parser.add_argument('-X', '--request')
        parser.add_argument('url')
        self._parser = parser

    def new(self):
        return Curl()

    def __del__(self):
        pass

    def _check_threshold(self):
        if self._max_time > 0 and time.time() - self._transfer_start_time > self._max_time:
            raise CurlError(Curl.CURLE_OPERATION_TIMEDOUT)
        if self._max_filesize > 0 and self._received_size > self._max_filesize:
            raise CurlError(Curl.CURLE_FILESIZE_EXCEEDED)

    def _read_line(self):
        pos = -1
        while True:
            pos = self._buf.find('\n')
            if pos >= 0:
                break
            data = self._conn.recv(RECV_PACKET_LEN)
            if data == '':
                break
            self._buf += data
            self._received_size += len(data)
            self._check_threshold()

        if pos == -1:
            return ''
        else:
            pos += 1
            line = self._buf[:pos]
            self._buf = self._buf[pos:]
            return line

    def _read(self, size=None):
        if size == None:
            while True:
                data = self._conn.recv(RECV_PACKET_LEN)
                if data == '':
                    break
                self._buf += data
                self._received_size += len(data)
                self._check_threshold()

            buf = self._buf
            self._buf = ''
            return buf
        buf_len = len(self._buf)
        if size == buf_len:
            buf = self._buf
            self._buf = ''
        elif size < buf_len:
            buf = self._buf[:size]
            self._buf = self._buf[size:]
        else:
            need = size - buf_len
            while need > 0:
                data = self._conn.recv(max(need, RECV_PACKET_LEN))
                if data == '':
                    break
                else:
                    self._buf += data
                    self._received_size += len(data)
                    self._check_threshold()
                    need -= len(data)

            if need > 0:
                buf = self._buf
                self._buf = ''
            else:
                buf = self._buf[:size]
                self._buf = self._buf[size:]
        return buf

    def _connect(self, host, port, timeout, isssl=False):
        conn = None
        try:
            if isssl and not _SUPPORT_SSL:
                raise 'Not SUPPORT SSL'
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.connect((host, port))
            if isssl:
                try:
                    conn = ssl.wrap_socket(conn, ssl_version=ssl.PROTOCOL_SSLv23)
                except ssl.SSLError as _:
                    conn.close()
                    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    conn.connect((host, port))
                    conn = ssl.wrap_socket(conn, ssl_version=ssl.PROTOCOL_SSLv2)

            conn.settimeout(timeout)
        except Exception as e:
            raise CurlError(Curl.CURLE_COULDNT_CONNECT)

        return conn

    def _make_request(self, raw, path, host):
        raw = str(raw)
        raw = raw.replace('\r\n', '\n')
        raw = raw.replace('\n', '\r\n')
        if raw.index('\r\n\r\n') == -1:
            raise CurlError(Curl.CURLE_ARG_ERROR)
        try:
            method = raw[:raw.index(' ')]
        except:
            raise CurlError(Curl.CURLE_ARG_ERROR)

        raw = re.sub('(\\w+ )([^ ]+)( HTTP)', '\\1%s\\3' % path, raw, 1)
        raw = re.sub('\\r\\nHost: *([\\w\\.]+)', '\\r\\nHost: %s' % host, raw, 1, flags=re.I)

        if self._init_cookie:
            if re.search('\\r\\nCookie: *', raw, flags=re.I):
                raw = re.sub('\\r\\nCookie: *([^\\r]+)', '\\r\\nCookie: \\1; %s' % self._init_cookie, raw, 1,
                             flags=re.I)
            else:
                raw = re.sub('(\\r\\n\\r\\n)', '\\r\\nCookie: %s\\1' % self._init_cookie, raw, 1)
        if re.search('\\r\\nConnection: *', raw, flags=re.I):
            raw = re.sub('\\r\\nConnection: *([\\w-]+)', '\\r\\nConnection: Keep-Alive', raw, 1, flags=re.I)
        else:
            raw = re.sub('(\\r\\n\\r\\n)', '\\r\\nConnection: Keep-Alive\\1', raw, 1)

        length = len(raw) - raw.index('\r\n\r\n') - 4
        raw = re.sub('\\r\\nContent-Length: *([\\w-]+)', '\\r\\nContent-Length: %d' % length, raw, 1, flags=re.I)

        return (raw, method)

    def _request(self, args):
        keep_alive_timeout = 0
        url = args.url
        if not (url.lower().find('http://') == 0 or url.lower().find('https://') == 0):
            url = 'http://' + url
        default_port = {'http': 80, 'https': 443}
        r = urlparse.urlparse(url)
        isssl = r.scheme == 'https' and args.proxy == None
        path = r.path

        if not path:
            path = '/'
        if r.scheme not in default_port:
            raise CurlError(Curl.CURLE_UNSUPPORTED_PROTOCOL)
        if r.query:
            path = path + '?' + r.query

        port = r.port
        host = r.hostname

        if port is None:
            port = default_port[r.scheme]
        else:
            port = int(port)

        is_reuse = False
        target = '%s:%d' % (r.hostname, port)
        conn = None
        self._buf = ''

        if args.proxy:
            connecthost = args.proxy[0]
            connectport = args.proxy[1]
        else:
            connecthost = host
            connectport = port

        for i in range(2):
            if target not in self._conn_pool:
                conn = self._connect(connecthost, connectport, args.connect_timeout, isssl)
            else:
                keep_alive_timeout = self._timeout_pool[target]

                if keep_alive_timeout == 0 or time.time() <= keep_alive_timeout:
                    conn = self._conn_pool[target]
                    is_reuse = True
                else:
                    continue

                del self._conn_pool[target]
                del self._timeout_pool[target]
            break

        if not conn:
            raise CurlError(Curl.CURLE_SEND_ERROR)
        conn.settimeout(20)
        self._conn = conn
        postdata = ''
        if args.raw:
            request, method = self._make_request(args.raw, url if args.proxy else path, host)
        else:
            method = None
            if args.request:
                method = args.request
            elif args.head:
                method = 'HEAD'
            elif args.upload_file:
                method = 'PUT'
            elif args.data:
                method = 'POST'
            else:
                method = 'GET'
            headers = {}
            if r.port:
                headers['Host'] = '%s:%d' % (r.hostname, port)
            else:
                headers['Host'] = r.hostname
            headers['User-Agent'] = args.user_agent
            if args.referer:
                headers['Referer'] = args.referer
            headers['Accept'] = '*/*'
            headers['Connection'] = 'Keep-Alive'
            if args.header:
                for line in args.header:
                    pos = line.find(':')
                    if pos > 0:
                        key = line[:pos]
                        val = line[pos + 1:].strip()
                        for k in headers:
                            if k.lower() == key.lower():
                                key = k
                                break
                        headers[key] = val

            if args.data:
                if len(args.data) == 1:
                    postdata = args.data[0]
                else:
                    for d in args.data:
                        if postdata != '':
                            postdata += '&'
                        postdata += d

                headers['Content-Length'] = str(len(postdata))
                if method == 'POST':
                    if not headers.has_key('Content-Type'):
                        headers['Content-Type'] = 'application/x-www-form-urlencoded'
            authinfo = None
            if args.user:
                authinfo = args.user
            if r.username:
                authinfo = r.username + ':' + r.password
            if authinfo:
                headers['Authorization'] = 'Basic ' + base64.b64encode(authinfo)
            cookie_str = str(self._init_cookie) if self._init_cookie else ''
            if target in self._cookie_pool:
                c = self._cookie_pool[target]
                for k in c.keys():
                    m = c[k]
                    if r.path.find(m['path']) != 0:
                        continue
                    expires = m['expires']
                    if not expires:
                        continue
                    if cookielib.http2time(expires) < time.time():
                        del c[k]

                cookie_str += c.output(attrs=[], header='', sep=';').strip()
            if args.cookie:
                if cookie_str:
                    cookie_str += '; ' + args.cookie
                else:
                    cookie_str = args.cookie
            if cookie_str:
                headers['Cookie'] = cookie_str
            if args.proxy:
                request = '%s %s HTTP/1.1\r\n' % (method, url)
            else:
                request = '%s %s HTTP/1.1\r\n' % (method, path)
            for k in headers:
                request += k + ': ' + headers[k] + '\r\n'

            request += '\r\n'
        response = ''
        content = ''
        msg = {}
        http_code = 0
        mime_type = None
        for i in range(2):
            msg = {}
            response = ''
            mime_type = None
            try:
                if args.upload_file:
                    conn.sendall(request)
                    line = self._read_line()
                    if line.find('100 Continue') != -1:
                        self._read_line()
                        conn.sendall(postdata)
                    else:
                        if response == '':
                            cut = line.split()
                            if len(cut) == 2:
                                http_code = int(cut[1])
                        response += line
                elif postdata:
                    conn.sendall(request + postdata)
                else:
                    conn.sendall(request)
            except:
                raise CurlError(Curl.CURLE_SEND_ERROR)

            try:
                while True:
                    line = self._read_line()
                    if line == '\r\n' or line == '\n':
                        response += line
                        break
                    elif line == '':
                        raise CurlError(Curl.CURLE_RECV_ERROR)
                    if response == '':
                        cut = line.split()
                        http_code = int(cut[1])
                    response += line
                    pos = line.find(':')
                    if pos == -1:
                        continue
                    end = line.find('\r')
                    key = line[:pos].lower()
                    val = line[pos + 1:end].strip()
                    msg[key] = val
                    if key == 'set-cookie':
                        if target in self._cookie_pool:
                            c = self._cookie_pool[target]
                        else:
                            c = Cookie.SimpleCookie()
                            self._cookie_pool[target] = c
                        c.load(val)
                    elif key == 'keep-alive':
                        m = RE_KEEPALIVE_TIMEOUT.search(val)
                        if m:
                            keep_alive_timeout = int(m.group(1))
                            if keep_alive_timeout > 0:
                                keep_alive_timeout += time.time()
                    elif args.mime_type and key == 'content-type':
                        m = RE_MIME_TYPE.search(val)
                        if m:
                            mime_type = m.group(1).strip()

            except CurlError as e:
                if i == 0 and is_reuse:
                    conn = self._connect(host, port, args.connect_timeout, isssl)
                else:
                    raise e
            else:
                break

        if args.mime_type and not (args.location and msg.has_key('location')):
            if not mime_type or mime_type.lower().find(args.mime_type.lower()) == -1:
                raise CurlError(Curl.CURLE_MIME_ERROR)
        if method != 'HEAD':
            if msg.get('transfer-encoding', None) == 'chunked':
                while True:
                    chunk_size = int(self._read_line(), 16)
                    if chunk_size > 0:
                        content += self._read(chunk_size)
                    self._read_line()
                    if chunk_size <= 0:
                        break

            else:
                content_len = msg.get('content-length', None)
                if content_len == None:
                    if http_code != 204:
                        content = self._read()
                elif content_len > 0:
                    content_len = int(content_len)
                    content = self._read(content_len)
                    if len(content) != content_len:
                        raise CurlError(Curl.CURLE_RECV_ERROR)
            encode = msg.get('content-encoding', None)
            if encode == 'gzip':
                content = gzip.GzipFile(fileobj=StringIO.StringIO(content)).read()
            elif encode == 'deflate':
                try:
                    content = zlib.decompress(content, -zlib.MAX_WBITS)
                except:
                    content = zlib.decompress(content)

        if msg.get('connection', '').find('close') != -1 or keep_alive_timeout > 0 and time.time() > keep_alive_timeout:
            conn.close()
        else:
            self._conn_pool[target] = conn
            self._timeout_pool[target] = keep_alive_timeout
        if msg.has_key('location') and args.location and (args.max_redirs == 0 or self._redirs < args.max_redirs):
            self._redirs += 1
            args.data = ''
            location_url = ''
            if msg['location'].startswith('http'):
                location_url = msg['location']
            elif msg['location'].startswith('/'):
                location_url = '%s://%s%s' % (r.scheme, r.netloc, msg['location'])
            if args.url != location_url:
                args.url = location_url
                return self._request(args)
        self._error_count = 0
        if self.sniff_func:
            self.sniff_func(args.url, response, content)
        return (http_code,
                response,
                content,
                0,
                url)

    def reset(self):
        self._cookie_pool = {}
        self._conn_pool = {}
        self._timeout_pool = {}

    def curl(self, cmdline):
        """
        code, head, body, ecode, redirect_url
        Args:
            cmdline: 

        Returns: code, head, body, ecode, redirect_url

        """
        t1 = time.time() * 1000
        code, head, body, ecode, redirect_url = range(5)
        if self._error_count > self._max_error:
            code, head, body, ecode, redirect_url = (0, '', '', Curl.CURLE_COULDNT_CONNECT, '')
        else:
            try:
                args = self._parser.parse_args(shlex.split(cmdline))
                args.proxy = None
                args.raw = None
                for i in range(args.retry + 1):
                    self._transfer_start_time = time.time()
                    self._redirs = 0
                    self._received_size = 0
                    self._max_filesize = args.max_filesize
                    self._max_time = args.max_time
                    if i > 0:
                        time.sleep(args.retry_delay)
                    try:
                        code, head, body, ecode, redirect_url = self._request(args)
                        break
                    except CurlError as e:
                        if i < args.retry and e.code in [Curl.CURLE_COULDNT_CONNECT, Curl.CURLE_RECV_ERROR]:
                            continue
                        self._error_count += 1
                        code, head, body, ecode, redirect_url = (0, '', '', e.code, args.url)
                        break
                    except Exception as e:
                        if i == args.retry:
                            code, head, body, ecode, redirect_url = (0, '', '', Curl.CURLE_RECV_ERROR, args.url)
                            break

            except:
                code, head, body, ecode, redirect_url = (0, '', '', Curl.CURLE_ARG_ERROR, '')

        t2 = time.time() * 1000
        if self.log_func:
            self.log_func.info('CurlLog {arg} {plugin_id} {time} {error}'.format(arg=cmdline, plugin_id=self.plugin_id,
                                                                                 time=int(t2 - t1), error=ecode))

        return code, head, body, ecode, redirect_url

    def curl2(self, url, post=None, **kwargs):
        """
        code, head, body, ecode, redirect_url
        Args:
            url: 
            post: 
            **kwargs: 

        Returns: code, head, body, ecode, redirect_url

        """
        global redirect_url
        t1 = time.time() * 1000
        code, head, body, ecode, redirect_url = range(5)
        if self._error_count > self._max_error:
            code, head, body, ecode, redirect_url = (0, '', '', Curl.CURLE_COULDNT_CONNECT, '')
        else:
            args = Namespace()
            args.url = url
            args.head = None
            args.upload_file = kwargs.get('upload-file')
            args.raw = kwargs.get('raw')
            args.request = kwargs.get('method')
            args.data = None
            if post:
                args.data = [post]
            args.cookie = kwargs.get('cookie')
            args.referer = kwargs.get('referer')
            args.user_agent = kwargs.get('user_agent') if kwargs.get('user_agent') else DEF_USER_AGENT
            args.header = [kwargs.get('header')] if kwargs.get('header') else None
            args.max_time = kwargs.get('max_time') if kwargs.get('max_time') != None else 0
            args.max_filesize = kwargs.get('max_filesize')
            args.mime_type = kwargs.get('mime_type')
            args.location = kwargs.get('location')
            args.connect_timeout = kwargs.get('connect_timeout') if kwargs.get('connect_timeout') != None else 10
            args.max_redirs = kwargs.get('max_redirs') if kwargs.get('max_redirs') != None else 5
            args.retry = kwargs.get('retry') if kwargs.get('retry') != None else 2
            args.retry_delay = kwargs.get('retry_delay') if kwargs.get('retry_delay') != None else 1
            args.user = kwargs.get('user')
            args.proxy = kwargs.get('proxy')
            for i in range(args.retry + 1):
                self._transfer_start_time = time.time()
                self._redirs = 0
                self._received_size = 0
                self._max_filesize = args.max_filesize
                self._max_time = args.max_time
                if i > 0:
                    time.sleep(args.retry_delay)
                try:
                    code, head, body, ecode, redirect_url = self._request(args)
                    break
                except CurlError as e:
                    if i < args.retry and e.code in [Curl.CURLE_COULDNT_CONNECT, Curl.CURLE_RECV_ERROR]:
                        continue
                    self._error_count += 1
                    code, head, body, ecode, redirect_url = (0, '', '', e.code, args.url)
                    break
                except Exception as e:
                    if i == args.retry:
                        code, head, body, ecode, redirect_url = (0, '', '', Curl.CURLE_RECV_ERROR, args.url)
                        break

        t2 = time.time() * 1000

        if self.log_func and None:
            self.log_func.info(
                'curllog {arg} {plugin_id} {time} {error}'.format(arg='%s\n%s\n%s' % (url, str(post), repr(kwargs)),
                                                                  plugin_id=self.plugin_id,
                                                                  time=int(t2 - t1), error=ecode))

        return code, head, body, ecode, redirect_url


if __name__ == '__main__':
    from dummy.logger import logger
    s = Curl(log_func=logger)

    code, head, body, errcode, final_url = s.curl2('http://baidu.com', method='GET', location=True, connect_timeout=0.2)
    print code, head, body, errcode, final_url
