#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '半块西瓜皮'

def assign(service, arg):
    if service == "wordpress":
        return True, arg
def audit(args):
    payload = 'wp-content/plugins/html5-mp3-player-with-playlist/html5plus/playlist.php'
    verify_url = args + payload
    code, head, content, errcode,finalurl = curl.curl(verify_url)
    if code ==200 and 'html5-mp3-player-with-playlist/html5plus/playlist.php' in content:
        security_info(verify_url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
