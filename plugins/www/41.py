#!/usr/bin/env python
import re
import urlparse

def assign(service, arg):
    if service != "www":
        return
    r = urlparse.urlparse(arg)
    return True, '%s://%s/' % (r.scheme, r.netloc)

def audit(arg):
    url = arg
    ret = False
    fuzz_url = url + '%3f.jsp'
    code, head, res, _, _ = curl.curl(fuzz_url)
    if code == 200 and res.find('<title>Directory of') != -1:
        ret = True
    else:
        fuzz_url = url + 'resin-doc/viewfile/?contextpath=/&servletpath=&file=fakefile.xml'
        code, head, res, _, _ = curl.curl(fuzz_url)
        if code == 200 and (res.find('not found /fakefile.xml') != -1 or \
                res.find('<title>fakefile.xml') != -1):
            ret = True

    if ret:
        security_warning(fuzz_url)

if __name__ == '__main__':
    from __loader import *
    audit(assign('www', 'http://www.abc.com/')[1])

