#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python

def assign(service, arg):
    if service == "appcms":
        return True, arg

def audit(arg):
    payload = 'backup/appcms.sql'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200:
        if ('SELECT' in res) or ('FORM' in res): 
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('appcms', 'http://localhost/')[1])