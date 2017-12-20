#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:
#Refer:http://www.wooyun.org/bugs/wooyun-2014-071575

def assign(service,arg):
    if service=="chengrui_edu":
        return True,arg 
    


def  audit(arg):
    url=arg+"log.txt"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'User' and 'Password' in res:
            security_hole(url)

if __name__=="__main__":
    from dummy import *

    audit(assign('chengrui_edu','http://demo.edudu.net/')[1])
    audit(assign('chengrui_edu','http://oa.jjzyzz.com/')[1])