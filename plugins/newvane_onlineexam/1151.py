#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2015-0108559

def assign(service, arg): 
    if service == "newvane_onlineexam":
        return True, arg
		
def audit(arg): 
    payloads = ['mana/edit/uploadattcah.jsp',
               'mana/edit/attach_upload.jsp',
               'mana/edit/uploadimg.jsp',
               'mana/edit/uploadmult.jsp',
               'mana/edit/uploadflash.jsp']
    for payload in payloads:
        code, head, res, errcode, _ = curl.curl2(arg+payload)
        if code == 200 and ('_upload.jsp' in res or 'uploadnexturl' in res):
            security_hole('Arbitrary file upload vulnerability '+ arg + payload)	
           
if __name__ == '__main__': 
    from dummy import *
    audit(assign('newvane_onlineexam', 'http://exam.kingdee.com/')[1])