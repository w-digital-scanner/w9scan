#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-061685 

def assign(service, arg):
    if service == 'pageadmin':
        return True, arg

def audit(arg):
    payload = 'e/database/v3.mdb'
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target)
    if code == 200 and 'Content-Type: application/x-msaccess'in head:
        security_warning(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('pageadmin', 'http://www.jixiangchansi.com/')[1])