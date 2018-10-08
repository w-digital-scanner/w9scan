#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# author:w8ay

import socket
import time

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    domain = util.get_domain_root(arg)
    
    tlds = util.list_from_file("database/sub_domain.txt")

    unable_pro = "sbsbsbsbforw9scanunablepro"
    hostnames = unable_pro + "." + domain
    hostnames = hostnames.strip()
    try:
        l = socket.gethostbyname_ex(hostnames)
    except socket.error:
        l = 0
    if l != 0:
        security_info("域名存在泛解析 %s" % ("*." + domain), 'subdomain')
        return

    for pro in tlds:
        hostnames = pro + "." + domain
        hostnames = hostnames.strip()
        try:
            l = socket.gethostbyname_ex(hostnames)
            security_info(str(l),'subdomain')
            time.sleep(0.01)
        except socket.error:
            pass

if __name__ == '__main__':
    from dummy import *

    audit("http://blog.hacking8.com/")
