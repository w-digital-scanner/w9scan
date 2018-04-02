#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# author:w8ay

import socket
def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    domain = util.get_domain_root(arg)
    
    tlds = util.list_from_file("database/sub_domain.txt")

    unable_pro = "sbsbsbsbforw9scanunable_pro"
    hostnames = unable_pro + "." + domain
    hostnames = hostnames.strip()
    try:
        l = socket.gethostbyname_ex(hostnames)
    except socket.error:
        pass
    if l:
        security_info("域名存在泛解析 %s"%("*." + domain),'subdomain')
        return 
    for pro in tlds:
        hostnames = pro + "." + domain
        hostnames = hostnames.strip()
        try:
            l = socket.gethostbyname_ex(hostnames)
            security_info(str(l),'subdomain')
        except socket.error:
            pass

if __name__ == '__main__':
    from dummy import *

    audit("https://bbs.125.la/aaaaaaa")
