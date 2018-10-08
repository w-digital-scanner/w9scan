#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'darkkid'
# Name:Discuz! X3 tools


def assign(service, arg):
    if service == "discuz":
        return True, arg


def audit(arg):
    payload = 'source/plugin/tools/tools.php'
    verify_url = arg + payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    if code == 200 and "Discuz" in res:
        security_warning(verify_url + ' Discuz! X3 tools')

if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz', 'http://www.example.com/')[1])