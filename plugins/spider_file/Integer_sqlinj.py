#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 只寻找int型的注入点

from dummy import *
import urlparse
import hashlib
from urllib import quote as urlencode
from urllib import unquote as urldecode
import os

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

    for i in parse.query.split('&'):
        if '=' not in i:
            continue
        k, v = i.split('=')
        if(util.is_number(v)):
            res_md5_1 = md5(html)
            url_1 = url.replace("%s=%s"%(k,v),"%s=%s"%(k,urlencode(v+'+1')))
            url_2 = url.replace("%s=%s"%(k,v),"%s=%s"%(k,urlencode(v+'+1-1')))
            try:
                code, head, html, redirect_url, log = hackhttp.http(url_1)
                res_md5_2 = md5(html)
                code, head, html, redirect_url, log = hackhttp.http(url_2)
                res_md5_3 = md5(html)
            except Exception, e:
                print e
                res_md5_1 = res_md5_2 = res_md5_3 = 0

            if (res_md5_1 == res_md5_3) and res_md5_1 != res_md5_2:
                security_hole(log["request"].replace(os.linesep,'</br>'),"Integer Sql injection:" + url)
            return

if __name__ == '__main__':
    url = "http://testphp.vulnweb.com/listproducts.php?artist=1"
    code, head, html, redirect_url, log = hackhttp.http(url)
    audit(url,html)