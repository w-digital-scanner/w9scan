#!/usr/bin/env python
import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    for p in [
        'wp-includes/registration-functions.php',
        'wp-includes/registration.php',
        'wp-includes/user.php',
        'wp-includes/rss-functions.php'
        ]:
        code, head, res, errcode, _ = curl.curl(url + p)
        debug('[%03d] %s', code, url+p)
        if code == 200:
            m = re.search('</b>:[^\r\n]+ in <b>([^<]+)</b> on line <b>(\d+)</b>', res)
            if m:
                security_info(m.group(1))
                break

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.taowr.com/')[1])
