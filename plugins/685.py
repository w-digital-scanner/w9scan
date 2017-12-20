#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Angel'


import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + "manager/html"    
    code, head, res, errcode, _ = curl.curl(url)
    if code == 401:
        task_push('www-auth', url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://ftp.kaova.net/')[1])