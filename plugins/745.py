#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  OGNL console
Author    :  a
mail        :  a@lcx.cc
Referer:	http://wooyun.org/bugs/wooyun-2010-080076
"""

import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = '/struts/webconsole.html'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
	
    if code == 200 and "Welcome to the OGNL console" in res:
        security_info('find ognl console:' +url)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://www.homilychart.com/')[1])
