#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: svn源码泄露扫描
referer: unknown
author: Lucifer
description: 忘记了删除.svn目录而导致的漏洞。
'''
def assign(service, arg):
    if service == "www":
        return True, arg

def audit(arg):
    payload = "/.svn/entries"
    vulnurl = arg + payload
    code, head, html, redirect_url, log = hackhttp.http(vulnurl)
    
    if r"dir" in html or r"file" in html and code==200:
        security_hole(u"svn源码泄露 payload:"+vulnurl)