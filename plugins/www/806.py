#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = DWBH
# __type__  = jboss 7未授权访问及弱口令检测
import urlparse
def assign(service, arg):
    if service != "www":
        return
    arr=urlparse.urlparse(arg)
    return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    payload = "management"
    target=arg+payload
    code, head, body, errcode, _ = curl.curl(target)
    if code == 200 and '.jboss.' in body:
        security_hole(target)
    if code ==401:
        task_push('www-auth',target)
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('www','http://192.168.0.116:9990/')[1])
