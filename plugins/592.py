#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = rabit2013
#_PlugName_ = avcon6 upload file

def assign(service, arg):
    if service == "avcon6":
        return True, arg

def audit(arg):
    payload = "/voip/basemanager/dorolldata"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and 'doRollback' in res:
        security_info(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('avcon6', 'http://avcon.icampus.cn:8080')[1])