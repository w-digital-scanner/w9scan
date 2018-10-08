#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:TCExam重新安装可getshell漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2013-046974


def assign(service,arg):
    if service=="tcexam":
        return True,arg 


def  audit(arg):
    url=arg+"install/install.php"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'db_user' in res and 'db_password' in res:
        security_hole(url)
if __name__=="__main__":
    from dummy import *
    audit(assign('tcexam','http://210.44.48.41:8080/')[1])
    audit(assign('tcexam','http://www.robotpartner.cn/')[1])
    audit(assign('tcexam','http://61.54.213.12:86/exam/')[1])