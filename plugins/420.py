#!/usr/bin/env python
import re

def assign(service, arg):
    if service == "wecenter":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + '?/search/ajax/search_result/')
    if code == 200:
        m = re.search('in(.+) on line', res)
        if m:
            security_info(m.group(1))

if __name__ == '__main__':
    from dummy import *
    audit(assign('wecenter', 'http://localhost:8080/wecenter/')[1])
