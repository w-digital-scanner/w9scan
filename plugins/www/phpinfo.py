#!/usr/bin/env python
import re
import urlparse


def assign(service, arg):
    if service == "www":
        return True, arg


def audit(arg):
    path = "/phpinfo.php"
    code, head, res, errcode, _ = curl.curl(arg + path)
    if code == 200 and "allow_url_fopen" in res:
        security_note("phpinfo leak:" + arg + path)


if __name__ == '__main__':
    from dummy import *

    audit(assign('www', 'http://blog.hacking8.com/')[1])
