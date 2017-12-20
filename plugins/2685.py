#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:浙大升腾软件开发的数字房产系统越权访问可以getshell
#Refer:http://www.wooyun.org/bugs/wooyun-2010-063656


def assign(service,arg):
    if service=="suntown_pm":
        return True,arg 


def  audit(arg):
    url=arg+"admini/upfile/upfile.aspx"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'PageA_name' in res and 'PageA_per' in res:
            security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('suntown_pm','http://web.jafdc.cn/')[1])
    audit(assign('suntown_pm','http://www.tgfgj.com/')[1])