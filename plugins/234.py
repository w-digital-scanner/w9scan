#!/usr/bin/env python
import re
import urlparse

def assign(service, arg):
    if service != "zhengfang":
        return
    return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'ftb.imagegallery.aspx')
    if code == 200:
        m = re.search('not found in <b>([^<]+)</b> on line <b>(\d+)</b>', res)
        if m:
            security_info(m.group(1))


if __name__ == '__main__':
    from dummy import *
    audit(assign('zhengfang', 'http://www.example.com/')[1])