#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
# ref:http://www.wooyun.org/bugs/wooyun-2014-066906
# ref:http://www.devttys0.com/2015/04/hacking-the-d-link-dir-890l/
# ref:http://www.freebuf.com/vuls/64521.html

import urlparse
def assign(service, arg):
    if service == "www":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    url = arg + "HNAP1/"
    header = 'SOAPAction: "http://purenetworks.com/HNAP1/GetWanSettings"'
    code, head, res, errcode, finalurl = curl.curl2(url,method='POST',header=header)
    if code == 200 and "xmlns:soap" in res:
        security_warning("D_link /HANP1 unauthenticated remote query information " + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://qq.com/')[1])