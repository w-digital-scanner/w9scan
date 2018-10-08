#!/usr/bin/env python
import re
import urlparse


def assign(service, arg):
    if service == "www":
        return True, arg


def audit(arg):
    path = "/WEB-INF/web.xml"
    code, head, res, errcode, _ = curl.curl(arg + path)
    if code == 200 and "<web-app" in res:
        security_note("存在TOMCAT web.xml泄露:" + arg + path)


if __name__ == '__main__':
    from dummy import *

    audit(assign('www', 'http://blog.hacking8.com/')[1])
