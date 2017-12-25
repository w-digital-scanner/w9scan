#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = rabit2013
#_PlugName_ = avcon6 upload file


def assign(service, arg):
    if service == "avcon6":
        return True, arg


def audit(arg):
    payload = "AvconWebService/fingerprint.jsp"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and "System Fingerprint" in res:
        security_info(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('avcon6', 'http://avol.nbtvu.net.cn:8080/')[1])