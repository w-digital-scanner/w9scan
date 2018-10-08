#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: crossdomain.xml文件发现
referer: unknown
author: Lucifer
description: crossdomain错误配置可导致。
'''
def assign(service, arg):
    if service == "www":
        return True, arg

def audit(arg):
    payload = "/crossdomain.xml"
    vulnurl = arg + payload
    try:
        code, head, html, redirect_url, log = hackhttp.http(vulnurl)
        if 'allow-access-from domain="*"' in html:
            security_note(u"存在crossdomain.xml文件发现漏洞...(信息) payload: "+vulnurl)
    except:
        pass