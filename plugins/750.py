#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : redis未授权访问
Author    : a
mail      :a@lcx.cc
危害及最新利用： 覆盖ssh密钥root登陆、数据库数据泄露、代码执行、敏感信息泄露
详情：http://www.freebuf.com/vuls/85188.html
"""

import socket

def assign(service, arg):
    if service == 'redis':
        return True, arg

def audit(arg):
    ip,port = arg
    payload = '\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a'
    try:
        s = socket.socket()
        s.connect((ip,port))
        s.send(payload)
        data = s.recv(1024)
        if 'redis_version' in data:
            security_hole( ip + ':' + str(port))
        s.close()
    except:
        pass
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('redis',('27.112.9.94',6379))[1])