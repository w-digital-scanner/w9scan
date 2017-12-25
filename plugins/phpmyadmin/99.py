#!/usr/bin/env python

def assign(service, arg):
    if service == 'phpmyadmin':
        return True, arg

def audit(arg):
    code, head, res, errcode, _ = curl.curl(arg + 'main.php')
    if code == 200 and res and res.find('MySQL client version') != -1 and res.find('root@localhost') != -1:
        security_hole(arg)


if __name__ == '__main__':
    from dummy import *
    audit(assign('phpmyadmin', 'http://union.fxaa.cc/old/')[1])

