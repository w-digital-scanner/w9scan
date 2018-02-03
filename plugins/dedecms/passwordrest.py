#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ref:https://www.t00ls.net/thread-43689-1-1.html

def assign(service, arg):
    if service == "dedecms":
        return True, arg

def audit(arg):
    url = arg
    code, head, body, redirect, log = hackhttp.http(arg + 'member/reg_new.php')
    if "系统关闭了会员功能" in body:
        return
    security_note("可能存在dede任意用户重置漏洞:https://www.t00ls.net/thread-43689-1-1.html")