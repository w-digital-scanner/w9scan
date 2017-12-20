#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Refer http://old.sebug.net/vuldb/ssvid-62693
import re

def assign(service, arg):
    if service == "eyou":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'user/send_queue/listCollege.php')
    if code == 200:
        r = re.search('MySQL result resource in <b>([^<]+)</b>',res)
        if r:
            security_info(r.group(1))

if __name__ == '__main__':
    from dummy import *
    audit(assign('eyou', 'http://mail.hzwk.cn/')[1])