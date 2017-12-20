#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  jenkins Command execution 
Author    :  a
mail      :  a@lcx.cc
Referer   : http://www.wooyun.org/bugs/wooyun-2010-094132
"""

import urlparse
def assign(service, arg):
    if service == 'jenkins':
        return True, arg

def audit(arg):
    payload = 'manage'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and  'pluginManager' in res:
        security_hole(url)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('jenkins', 'http://107.170.158.19:8080')[1])