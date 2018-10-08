#!/usr/bin/env python
import re
import urlparse


def assign(service, arg):
    if service == "www":
        return True, arg


def audit(arg):
    path = "/robots.txt/.php"
    code, head, res, errcode, _ = curl.curl(arg + path)
    if code == 200 and "User-agent" in res:
        security_note("存在解析漏洞:" + arg + path)


if __name__ == '__main__':
    from dummy import *

    audit(assign('www', 'http://blog.hacking8.com/')[1])
