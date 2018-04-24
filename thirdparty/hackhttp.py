#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Queue
import urlparse
import httplib
import ssl
import zlib
import gzip
import StringIO
import re
import threading
import mimetools
import Cookie
import cookielib
import copy
import time
import string


class httpheader(mimetools.Message):
    def __init__(self, fp, seekable=1):
        mimetools.Message.__init__(self, fp, seekable)

    def isheader(self, line):
        i = line.find(':')
        if i > -1:
            return line[:i]
        return None


class Compatibleheader(str):
    def setdict(self, d):
        self.dict = d

    def __getitem__(self, key):
        return self.dict.__getitem__(key)

    def get(self, key, d=None):
        return self.dict.get(key, d)


class MorselHook(Cookie.Morsel):
    """
    Support ":" in Cookie key.

    >>> import inspect
    >>> (inspect.getargspec(MorselHook.set)[3])[0]
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+-.^_`|~:"
    >>> cookie = Cookie.SimpleCookie()
    >>> cookie.load("key:key=abc; key=val")
    >>> print cookie
    Set-Cookie: key=val;
    Set-Cookie: key:key=abc;
    """
    def set(
        self, key, val, coded_val,
            LegalChars=Cookie._LegalChars + ':',
            idmap=string._idmap, translate=string.translate):
        return super(MorselHook, self).set(
            key, val, coded_val, LegalChars, idmap, translate)


class httpconpool():
    # 创建的连接总数, key 为 conhash
    connected = {}
    # 存放空闲连接的队列, key 为 conhash
    connectpool = {}
    # 存放 cookie 的池子，key 为 host
    maxconnectpool = 20
    lock = threading.Lock()

    def __init__(self, maxconnectpool=20, timeout=10):
        self.maxconnectpool = maxconnectpool
        self.timeout = timeout
        self.protocol = []
        self._get_protocol()

    def _get_protocol(self):
        if not self.protocol:
            ps = (
                'PROTOCOL_SSLv3', 'PROTOCOL_SSLv23', 'PROTOCOL_TLSv1',
                'PROTOCOL_SSLv2', 'PROTOCOL_TLSv1_1', 'PROTOCOL_TLSv1_2')
            for p in ps:
                pa = getattr(ssl, p, None)
                if pa:
                    self.protocol.append(pa)

    def _make_connect(self, https, host, port, proxy=None):
        if not https:
            if proxy:
                con = httplib.HTTPConnection(
                    proxy[0], proxy[1], timeout=self.timeout)
                con.set_tunnel(host, port)
            else:
                con = httplib.HTTPConnection(host, port, timeout=self.timeout)
            # con .set_debuglevel(2) #?
            con.connect()
            return con
        for p in self.protocol:
            context = ssl._create_unverified_context(p)
            try:
                if proxy:

                    con = httplib.HTTPSConnection(
                        proxy[0], proxy[1], context=context,
                        timeout=self.timeout)
                    con.set_tunnel(host, port)
                else:
                    con = httplib.HTTPSConnection(
                        host, port, context=context, timeout=self.timeout)
                con.connect()
                return con
            except ssl.SSLError, e:
                # print e,protocol
                pass
        raise Exception('connect err')

    def _get_connect(self, url, proxy):
        https, host, port, path = url
        conhash = '%d_%s_%d' % (https, host, port)
        self.lock.acquire()
        try:
            count = self.connected.get(conhash, 0)
            if count == 0:
                self.connected[conhash] = 0
            if not self.connectpool.get(conhash, None):
                self.connectpool[conhash] = Queue.Queue()
            if count <= self.maxconnectpool:
                if self.connectpool[conhash].qsize() == 0:
                    con = self._make_connect(https, host, port, proxy)
                    self.connected[conhash] += 1
                    self.connectpool[conhash].put(con)
        except:
            raise
        finally:
            self.lock.release()
        return self.connectpool[conhash].get()

    def _put_connect(self, url, con):
        https, host, port, path = url
        conhash = '%d_%s_%d' % (https, host, port)
        self.connectpool[conhash].put(con)

    def _release_connect(self, url):
        https, host, port, path = url
        conhash = '%d_%s_%d' % (https, host, port)
        self.lock.acquire()
        self.connected[conhash] -= 1
        self.lock.release()


class hackhttp():

    def __init__(self, conpool=None, cookie_str=None, throw_exception=True,user_agent = None,headers=None):
        """conpool: 创建的连接池最大数量，类型为 int，默认为 10

            cookie_str: 用户自己定义的 Cookie，类型为 String

            throw_exception: 是否抛出遇到的异常，类型为 bool，默认为 True

            为了全局配置useragent header 这里加入相关选项
        """
        self.throw_exception = throw_exception
        if conpool is None:
            self.conpool = httpconpool(10)
        else:
            self.conpool = conpool
        Cookie.Morsel = MorselHook
        self.initcookie = Cookie.SimpleCookie()
        if cookie_str:
            if not cookie_str.endswith(';'):
                cookie_str += ";"
            for cookiepart in cookie_str.split(";"):
                if cookiepart.strip() != "":
                    cookiekey, cookievalue = cookiepart.split("=", 1)
                    self.initcookie[cookiekey.strip()] = cookievalue.strip()
        self.cookiepool = {}
        self.user_agent = user_agent
        self.headers = headers

    def _get_urlinfo(self, url):
        p = urlparse.urlparse(url)
        scheme = p.scheme.lower()
        if scheme != 'http' and scheme != 'https':
            raise Exception('http/https only')
        host = p.hostname
        port = p.port
        https = True if scheme == "https" else False
        if not port:
            port = 443 if https else 80
        path = ''
        if p.path:
            path = p.path
            if p.query:
                path = path + '?' + p.query
        return https, host, port, path

    def _decode_html(self, head, body):
        # 这里处理编码有问题，所以暂不处理
        # return body
        if 'text' not in head:
            return body
        charset = None
        r = re.search(r'charset=(\S+)', head, re.I)
        if not r:
            r = re.search(r'charset=[\'"]*([^\r\n\'">]+)', body, re.I)
        if r:
            charset = r.group(1).lower()
            if charset == 'utf-8':
                return body
        else:
            charset = 'utf-8'
        try:
            body = body.decode(charset, 'ignore').encode('utf-8')
        except:
            pass
        return body

    def _send_output(self, oldfun, con, log):
        def _send_output_hook(*args, **kwargs):
            log['request'] = "\r\n".join(con._buffer)
            oldfun(*args, **kwargs)
            con._send_output = oldfun
        return _send_output_hook

    def http(self, url, post=None, **kwargs):
        r'''hh.http(...) -> (code, head, html, redirtct_url, log)

        Send an HTTP Request.

        kwargs:

            *********

            param: post: Set http POST data.

            eg:
                post = "key1=val1&key2=val2"

            *********

            param: header:
            param: headers:  Set http headers. If you set header, headers will drop.

            eg:

                header = 'Referer:https://bugscan.net\r\nUser-Agent: hackhttp user-agent'

            eg:
                headers={
                    'Referer': 'https://bugscan.net',
                    'User-Agent': 'hackhttp user-agent'
                }

            *********

            param: method: Set HTTP Request Method, default value is 'GET'.
            If the param "post" is set, the method will auto change to 'POST'
            The value of this param you can find it in RFC2616.

            Method List:
                OPTIONS, GET, HEAD, POST,
                PUT, DELETE, TRACE, CONNECT

            eg:
                method = 'POST'

            *********

            param: raw: Set HTTP raw package.

            eg:
                raw = """POST /post HTTP/1.1
                Host: httpbin.org
                User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0
                Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
                Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
                Accept-Encoding: gzip, deflate
                Connection: close
                Content-Type: application/x-www-form-urlencoded
                Content-Length: 19

                key1=val1&key2=val2"""

            *********

            param: proxy: Set HTTP Proxy, support http protocol.

            eg:
                proxy = ('127.0.0.1', 9119)

            *********

            param:cookcookie: Auto set cookie and get cookie.

            cookcookie=True

            *********

            param: location: Auto redirect when 302.

            eg:
                location=True

            *********

            param: throw_exception: Throw exception or pass when exception occurred.
            eg:
                throw_exception=True

            *********

            param: data: HTTP Request Data，when param is None.

            eg, application/x-www-form-urlencoded :

                data="key1=val1&key2=val2"

            eg, application/json:

                data='{"key1": "val1", "key2": "val2"}'

        '''
        headers = kwargs.get('header', '') or kwargs.get('headers', {})
        method = kwargs.get('method', None)
        raw = kwargs.get('raw', None)
        proxy = kwargs.get('proxy', None)
        if not post:
            post = kwargs.get('data', None)
        if type(post) == unicode:
            post = post.encode('utf-8', 'ignore')
        if type(raw) == unicode:
            raw = raw.encode('utf-8', 'ignore')
        cookcookie = kwargs.get('cookcookie', True)
        location = kwargs.get('location', True)
        throw_exception = kwargs.get('throw_exception', self.throw_exception)

        if not headers and self.headers:
            headers = self.headers
            
        if self.user_agent is not None and kwargs.get('user_agent', None) is None:
            kwargs["user_agent"] = self.user_agent

        if headers and (isinstance(headers, str) or isinstance(headers, unicode)):
            headers = httpheader(StringIO.StringIO(headers), 0).dict
        for arg_key, h in[
                ('cookie', 'Cookie'),
                ('referer', 'Referer'),
                ('user_agent', 'User-Agent'), ]:
            if kwargs.get(arg_key):
                headers[h] = kwargs.get(arg_key)

        try:
            if raw:
                return self.httpraw(
                    url, raw=raw, proxy=proxy, cookcookie=cookcookie,
                    location=location)
            else:
                return self._http(
                    url, post=post, headers=headers, method=method,
                    proxy=proxy, cookcookie=cookcookie,
                    location=location, locationcount=0)
        except:
            if throw_exception:
                raise
            else:
                return 0, '', '', '', {'url': '', 'request': '', 'response': ''}

    def _http(
            self, url, post=None, headers={}, method=None,
            proxy=None, cookcookie=True, location=True, locationcount=0):

        if not method:
            if post:
                method = "POST"
            else:
                method = "GET"
        rep = None
        urlinfo = https, host, port, path = self._get_urlinfo(url)
        log = {}
        con = self.conpool._get_connect(urlinfo, proxy)
        # con .set_debuglevel(2) #?
        conerr = False
        try:
            con._send_output = self._send_output(con._send_output, con, log)
            tmpheaders = copy.deepcopy(headers)
            tmpheaders['Accept-Encoding'] = 'gzip, deflate'
            tmpheaders['Connection'] = 'Keep-Alive'
            tmpheaders['User-Agent'] = tmpheaders['User-Agent'] if tmpheaders.get('User-Agent') else 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'

            if cookcookie:
                c = self.cookiepool.get(host, None)
                if not c:
                    self.cookiepool[host] = self.initcookie
                    c = self.cookiepool.get(host)
                if 'Cookie' in tmpheaders:
                    cookie_str = tmpheaders['Cookie'].strip()
                    if not cookie_str.endswith(';'):
                        cookie_str += ";"
                    for cookiepart in cookie_str.split(";"):
                        if cookiepart.strip() != "":
                            cookiekey, cookievalue = cookiepart.split("=", 1)
                            c[cookiekey.strip()] = cookievalue.strip()
                for k in c.keys():
                    m = c[k]
                    # check cookie path
                    if path.find(m['path']) != 0:
                        continue
                    expires = m['expires']
                    if not expires:
                        continue
                    # check cookie expires time
                    if cookielib.http2time(expires) < time.time():
                        del c[k]
                cookie_str = c.output(attrs=[], header='', sep=';').strip()
                if cookie_str:
                    tmpheaders['Cookie'] = cookie_str
            if post:
                tmpheaders['Content-Type'] = tmpheaders.get(
                    'Content-Type', 'application/x-www-form-urlencoded')
            else:
                # content-length err 411
                tmpheaders[
                    'Content-Length'] = tmpheaders.get('Content-Length', 0)
                if method == 'GET':
                    del tmpheaders['Content-Length']
            con.request(method, path, post, tmpheaders)
            rep = con.getresponse()
            body = rep.read()
            encode = rep.msg.get('content-encoding', None)
            if encode == 'gzip':
                body = gzip.GzipFile(fileobj=StringIO.StringIO(body)).read()
            elif encode == 'deflate':
                try:
                    body = zlib.decompress(body, -zlib.MAX_WBITS)
                except:
                    body = zlib.decompress(body)
            body = self._decode_html(
                rep.msg.dict.get('content-type', ''), body)
            retheader = Compatibleheader(str(rep.msg))
            retheader.setdict(rep.msg.dict)
            redirect = rep.msg.dict.get('location', url)
            if not redirect.startswith('http'):
                redirect = urlparse.urljoin(url, redirect)
            if cookcookie and "set-cookie" in rep.msg.dict:
                c = self.cookiepool[host]
                c.load(rep.msg.dict['set-cookie'])
        except httplib.ImproperConnectionState:
            conerr = True
            raise
        except:
            raise
        finally:
            if conerr or (rep and rep.msg.get('connection') == 'close') or proxy:
                self.conpool._release_connect(urlinfo)
                con.close()
            else:
                self.conpool._put_connect(urlinfo, con)

        log["url"] = url
        if post:
            log['request'] += "\r\n\r\n" + post
        log["response"] = "HTTP/%.1f %d %s" % (
            rep.version * 0.1, rep.status,
            rep.reason) + '\r\n' + str(retheader) + '\r\n' + (body[:4096])
        if location and url != redirect and locationcount < 5:
            method = 'HEAD' if method == 'HEAD' else 'GET'
            a, b, c, d, e = self._http(
                redirect, method=method, proxy=proxy,
                cookcookie=cookcookie, location=location,
                locationcount=locationcount + 1)
            log["response"] = e["response"]
            return a, b, c, d, log
        return rep.status, retheader, body, redirect, log

    def httpraw(self, url, raw, proxy=None, cookcookie=True, location=True):
        urlinfo = https, host, port, path = self._get_urlinfo(url)
        raw = StringIO.StringIO(raw.lstrip())
        requestline = raw.readline().rstrip()
        words = requestline.split()
        if len(words) == 3:
            command, _, _ = words
        elif len(words) == 2:
            command, _ = words
        else:
            raise Exception('http raw parse error')
        headers = httpheader(raw, 0).dict
        rawbody = ''
        content_type = headers.get('Content-Type', "")
        # Content-Type: application/x-www-form-urlencoded
        # Content-Type: multipart/form-data
        if content_type.startswith('application/x-www-form-urlencoded'):
            while 1:
                line = raw.readline()
                if line == '':
                    rawbody = rawbody[:-2]
                    break
                rawbody += line.rstrip() + '\r\n'
        if content_type.startswith('multipart/form-data'):
            while 1:
                line = raw.readline()
                if line == '':
                    break
                if line[:2] == "--":
                    if rawbody != "" and rawbody[-2:] != '\r\n':
                        rawbody = rawbody[:-1] + '\r\n'
                    rawbody += line.rstrip() + '\r\n'
                elif line[:8].lower() == 'content-':
                    rawbody += line.rstrip() + '\r\n'
                    line = raw.readline()
                    if line[:8].lower() == 'content-':
                        rawbody += line.rstrip() + '\r\n'
                        raw.readline()
                    rawbody += '\r\n'
                else:
                    rawbody += line
        headers['Host'] = host
        headers['Content-Length'] = str(len(rawbody))
        return self._http(
            url, post=rawbody, headers=headers, method=command,
            proxy=proxy, cookcookie=cookcookie, location=location)