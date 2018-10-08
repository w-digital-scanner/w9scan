#!/usr/bin/env python
#-*- coding: utf-8 -*-
import re
def assign(service, arg):
    if service == "phpshe":
        return True, arg


def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + '/module/index/index.php')
    if code == 200:
        m = re.search('in <b>([^<]+)</b>', res)
        if m:
            security_info(m.group(1))


if __name__ == '__main__':
    from dummy import *
    audit(assign('phpshe', 'http://www.jtdsc.com')[1])