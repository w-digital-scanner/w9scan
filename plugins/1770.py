#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer: http://www.wooyun.org/bugs/wooyun-2010-0121875

def assign(service, arg):
    if service == "ewebs":
        return True, arg

def audit(arg):
    vul_url = arg + 'testweb.php'
    code, _, body, _, _ = curl.curl2(vul_url)
    if code == 200 and '<td>access.log</td>' in body:
        security_warning(vul_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ewebs', 'http://60.190.163.51:8888/')[1])