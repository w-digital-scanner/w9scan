#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2010-043380

import urlparse
def assign(service, arg): 
    if service == "fsmcms":
        return True, arg
		
def audit(arg): 
    payload = '/setup/index.jsp'
    code, head, res, errcode, _ = curl.curl2(arg+payload)
    if code == 200 and '</font><input type="text" name="SetUpPath"' in res :
        security_hole('FSMCMS网站重装漏洞 '+ arg + payload)
 
if __name__ == '__main__': 
    from dummy import *
    audit(assign('fsmcms', 'http://www.wuda.gov.cn/')[1])
	
